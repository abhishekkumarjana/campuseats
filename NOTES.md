# CampusEats Orders REST Service

## Team Members

1. Name: ____ABHISHEK KUMAR JANA______________   Roll No: ____20252651002___
2. Name: ___TUSHAR BHARDHAJ   ROLL:_____20252651058__________
. Name: _____ASHISH KUMAR SINGH_______________   Roll No: 20252651014____________________
2. Name: ___BIKASH PRADHAN_________________   Roll No: ________20252651014____________
---

# Part A — Model the Service

## A2. SOAP-style Operations

The operations that could have been written in SOAP style are:

1. `placeOrder(studentId, items, deliveryAddressId, paymentMethodId)`
2. `getOrder(orderId)`
3. `listOrders(studentId, status)`
4. `cancelOrder(orderId, reason)`

These operations are used only as the starting point for designing the REST resources.

---

## A4. REST Resource Table

| Method | URL | What it does | Success Code | Failure Codes |
|---|---|---|---|---|
| POST | `/orders` | Creates a new order | 201 | 400, 409, 422, 503 |
| GET | `/orders/{orderId}` | Returns one order | 200 | 404 |
| GET | `/orders?studentId=...&status=...` | Returns filtered orders | 200 | 400 |
| POST | `/orders/{orderId}/cancellation` | Requests cancellation of an order | 202 | 400, 404, 409, 422 |

---

## A5. Hard Resource-Mapping Choice

The operation that mapped least comfortably to a REST resource was `cancelOrder(orderId, reason)`.

Instead of creating a verb-based URL such as `/orders/{orderId}/cancel`, cancellation is represented as a sub-resource using `/orders/{orderId}/cancellation`. This treats the cancellation as a state-changing resource associated with the order. We rejected `/cancelOrder` because REST URLs should represent resources rather than actions.

---

# Part D — Fallback Reasoning

The Orders service calls the Payments service when an order requires payment processing. If Payments is unreachable, the Orders service will fail the request rather than pretending that payment succeeded.

Degrading by creating a successfully paid order without confirmation from Payments would be incorrect because it could leave the order and payment state inconsistent. A timeout and retry will be used for safe transient failures, but if the dependency remains unavailable, the client receives an appropriate error response.

---

# Assignment 3 Comparison

## 1. WSDL vs OpenAPI

Assignment 3 described the service using a SOAP/WSDL contract, while this assignment describes the Orders service using OpenAPI.

WSDL contains SOAP-specific details such as the SOAP binding and operation/message definitions that are not required in the REST OpenAPI contract.

The difference in line count is:

- Assignment 3 WSDL: ______ lines
- Assignment 4 `openapi.yaml`: ______ lines
- Difference: ______ lines

The difference is mainly caused by the different protocol models. REST/OpenAPI describes HTTP resources, methods, parameters and HTTP responses directly instead of describing SOAP messages and bindings.

Two things declared by WSDL that OpenAPI does not need are:

1. SOAP binding information.
2. SOAP message/envelope-oriented operation definitions.

---

## 2. SOAP Fault vs REST Problem Response

One SOAP Fault from Assignment 3 was:

```xml
<soap:Fault>
    <faultcode>soap:Client</faultcode>
    <faultstring>Payment was declined</faultstring>
    <detail>
        <pay:PaymentError>
            <pay:errorCode>card_declined</pay:errorCode>
            <pay:errorMessage>The payment card was declined.</pay:errorMessage>
        </pay:PaymentError>
    </detail>
</soap:Fault>
In the REST service, this failure is replaced by HTTP status code `422` and
the common problem response:

```json
{
  "type": "https://campuseats.example/problems/payment-declined",
  "title": "Payment Declined",
  "status": 422,
  "detail": "The payment card was declined."
}