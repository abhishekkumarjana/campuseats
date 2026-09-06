import pytest

from app import app, store


@pytest.fixture(autouse=True)
def reset_store():
    store.orders.clear()
    store.idempotency_keys.clear()
    store.next_id = 1


@pytest.fixture
def client(monkeypatch):
    def fake_payment(*args, **kwargs):
        return {
            "success": True,
            "status": 200,
            "detail": "Payment successful."
        }

    monkeypatch.setattr("app.charge_payment", fake_payment)

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_create_order_success(client):
    response = client.post(
        "/orders",
        json={
            "studentId": "student-101",
            "items": [
                {
                    "itemId": "item-1",
                    "quantity": 2
                }
            ],
            "deliveryAddressId": "address-1",
            "paymentMethodId": "card-1"
        },
        headers={
            "Idempotency-Key": "order-key-001"
        }
    )

    assert response.status_code == 201
    assert response.headers["Location"] == "/orders/1"


def test_idempotent_repeat_returns_original(client):
    request_data = {
        "studentId": "student-101",
        "items": [
            {
                "itemId": "item-1",
                "quantity": 1
            }
        ],
        "deliveryAddressId": "address-1",
        "paymentMethodId": "card-1"
    }

    headers = {
        "Idempotency-Key": "order-key-002"
    }

    first_response = client.post(
        "/orders",
        json=request_data,
        headers=headers
    )

    second_response = client.post(
        "/orders",
        json=request_data,
        headers=headers
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 201
    assert first_response.get_json() == second_response.get_json()
    assert first_response.headers["Location"] == second_response.headers["Location"]

    assert len(store.orders) == 1


def test_malformed_body_returns_400(client):
    response = client.post(
        "/orders",
        json={
            "studentId": "student-101"
        },
        headers={
            "Idempotency-Key": "order-key-003"
        }
    )

    assert response.status_code == 400

    body = response.get_json()

    assert body["type"]
    assert body["title"]
    assert body["status"] == 400
    assert body["detail"]


def test_unknown_order_returns_404(client):
    response = client.get("/orders/999")

    assert response.status_code == 404

    body = response.get_json()

    assert body["type"]
    assert body["title"] == "Order Not Found"
    assert body["status"] == 404
    assert body["detail"]