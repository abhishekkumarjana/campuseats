from flask import Flask, request, jsonify, make_response
from models import Order
from store import OrderStore
from errors import problem
from payments_client import charge_payment


app = Flask(__name__)
store = OrderStore()


# -----------------------------
# Validation
# -----------------------------

def validate_create_order(data):
    if not isinstance(data, dict):
        return "Request body must be a JSON object."

    required_fields = [
        "studentId",
        "items",
        "deliveryAddressId",
        "paymentMethodId"
    ]

    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"

    if not isinstance(data["studentId"], str) or not data["studentId"].strip():
        return "studentId must be a non-empty string."

    if not isinstance(data["items"], list) or len(data["items"]) == 0:
        return "items must be a non-empty list."

    for item in data["items"]:
        if not isinstance(item, dict):
            return "Each item must be an object."

        if "itemId" not in item or "quantity" not in item:
            return "Each item must contain itemId and quantity."

        if not isinstance(item["itemId"], str) or not item["itemId"].strip():
            return "itemId must be a non-empty string."

        if not isinstance(item["quantity"], int) or item["quantity"] < 1:
            return "quantity must be an integer greater than zero."

    if not isinstance(data["deliveryAddressId"], str) or not data["deliveryAddressId"].strip():
        return "deliveryAddressId must be a non-empty string."

    if not isinstance(data["paymentMethodId"], str) or not data["paymentMethodId"].strip():
        return "paymentMethodId must be a non-empty string."

    return None


def validate_cancel_order(data):
    if not isinstance(data, dict):
        return "Request body must be a JSON object."

    if "reason" not in data:
        return "Missing required field: reason."

    if not isinstance(data["reason"], str) or not data["reason"].strip():
        return "reason must be a non-empty string."

    return None


# -----------------------------
# POST /orders
# -----------------------------

@app.route("/orders", methods=["POST"])
def create_order():

    # Validate the complete body BEFORE accessing its fields.
    data = request.get_json(silent=True)

    validation_error = validate_create_order(data)

    if validation_error:
        return problem(
            "https://campuseats.example/problems/malformed-request",
            "Malformed Request",
            400,
            validation_error
        )

    idempotency_key = request.headers.get("Idempotency-Key")

    if not idempotency_key:
        return problem(
            "https://campuseats.example/problems/missing-idempotency-key",
            "Missing Idempotency-Key",
            400,
            "Idempotency-Key header is required."
        )

    # Return the original result for a repeated request.
    existing_order = store.find_by_idempotency_key(idempotency_key)

    if existing_order:
        response = make_response(
            jsonify(existing_order.as_json()),
            201
        )
        response.headers["Location"] = f"/orders/{existing_order.order_id}"
        return response

    # Calculate a simple total for this demonstration.
    total = sum(item["quantity"] * 10.0 for item in data["items"])

    # Call Payments before storing the order.
    payment_result = charge_payment(
        payment_url=None,
        order_id=idempotency_key,
        amount=total,
        currency="INR",
        idempotency_key=idempotency_key
    )

    if not payment_result["success"]:

        if payment_result["status"] == 422:
            return problem(
                "https://campuseats.example/problems/payment-declined",
                "Payment Declined",
                422,
                payment_result["detail"]
            )

        return problem(
            "https://campuseats.example/problems/payment-service-unavailable",
            "Payment Service Unavailable",
            503,
            payment_result["detail"]
        )

    order = Order(
        order_id=None,
        student_id=data["studentId"],
        items=data["items"],
        delivery_address_id=data["deliveryAddressId"],
        payment_method_id=data["paymentMethodId"],
        status="PAID",
        total=total,
        idempotency_key=idempotency_key
    )

    store.create(order)

    response = make_response(
        jsonify(order.as_json()),
        201
    )

    response.headers["Location"] = f"/orders/{order.order_id}"

    return response


# -----------------------------
# GET /orders/{order_id}
# -----------------------------

@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):

    order = store.get(order_id)

    if order is None:
        return problem(
            "https://campuseats.example/problems/order-not-found",
            "Order Not Found",
            404,
            f"Order {order_id} does not exist."
        )

    return jsonify(order.as_json()), 200


# -----------------------------
# GET /orders
# -----------------------------

@app.route("/orders", methods=["GET"])
def list_orders():

    student_id = request.args.get("studentId")
    status = request.args.get("status")

    allowed_statuses = {
        "CREATED",
        "PAID",
        "CANCELLED"
    }

    if status and status not in allowed_statuses:
        return problem(
            "https://campuseats.example/problems/invalid-status",
            "Invalid Status",
            400,
            "status must be CREATED, PAID or CANCELLED."
        )

    orders = store.list_orders(
        student_id=student_id,
        status=status
    )

    return jsonify({
        "orders": [order.as_json() for order in orders]
    }), 200


# -----------------------------
# POST /orders/{order_id}/cancellation
# -----------------------------

@app.route("/orders/<int:order_id>/cancellation", methods=["POST"])
def cancel_order(order_id):

    data = request.get_json(silent=True)

    # Validate before accessing body fields.
    validation_error = validate_cancel_order(data)

    if validation_error:
        return problem(
            "https://campuseats.example/problems/malformed-request",
            "Malformed Request",
            400,
            validation_error
        )

    order = store.get(order_id)

    if order is None:
        return problem(
            "https://campuseats.example/problems/order-not-found",
            "Order Not Found",
            404,
            f"Order {order_id} does not exist."
        )

    if order.status == "CANCELLED":
        return problem(
            "https://campuseats.example/problems/order-state-conflict",
            "Order State Conflict",
            409,
            "The order has already been cancelled."
        )

    if order.status != "PAID":
        return problem(
            "https://campuseats.example/problems/order-cannot-be-cancelled",
            "Order Cannot Be Cancelled",
            422,
            "The order cannot be cancelled in its current state."
        )

    order.status = "CANCELLED"
    store.update(order)

    return jsonify(order.as_json()), 202


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)