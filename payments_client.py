import os
import random
import time

import requests


def charge_payment(
    payment_url,
    order_id,
    amount,
    currency,
    idempotency_key
):
    # Resolve the Payments service address from an environment variable.
    base_url = payment_url or os.getenv("PAYMENTS_URL")

    if not base_url:
        return {
            "success": False,
            "status": 503,
            "detail": "PAYMENTS_URL is not configured."
        }

    url = f"{base_url}/payments"

    payload = {
        "orderId": order_id,
        "amount": amount,
        "currency": currency
    }

    headers = {
        "Idempotency-Key": idempotency_key
    }

    max_attempts = 3
    base_delay = 0.2

    for attempt in range(max_attempts):

        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=2
            )

            # Never retry a 4xx response.
            if 400 <= response.status_code < 500:
                return {
                    "success": False,
                    "status": 422,
                    "detail": "Payment was rejected by the payment service."
                }

            # Retry transient 5xx responses.
            if 500 <= response.status_code < 600:

                if attempt == max_attempts - 1:
                    return {
                        "success": False,
                        "status": 503,
                        "detail": "Payment service is unavailable."
                    }

                delay = base_delay * (2 ** attempt)
                jitter = random.uniform(0, 0.1)

                time.sleep(delay + jitter)
                continue

            # Successful payment.
            if 200 <= response.status_code < 300:
                return {
                    "success": True,
                    "status": response.status_code,
                    "detail": "Payment successful."
                }

            return {
                "success": False,
                "status": 503,
                "detail": "Unexpected response from payment service."
            }

        except requests.RequestException:

            if attempt == max_attempts - 1:
                return {
                    "success": False,
                    "status": 503,
                    "detail": "Payment service is unreachable."
                }

            delay = base_delay * (2 ** attempt)
            jitter = random.uniform(0, 0.1)

            time.sleep(delay + jitter)

    return {
        "success": False,
        "status": 503,
        "detail": "Payment service is unavailable."
    }