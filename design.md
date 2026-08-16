# CampusEats — Services, Contracts & Schema Design

## 1. Capabilities

CampusEats provides the following main capabilities:

* View and search food menu
* View food details
* Add food to cart
* Remove food from cart
* Place an order
* Make payment
* Cancel an order
* Track an order
* Add, update and remove food items
* Update food availability
* Manage users and vendors

## 2. Service Design

### Catalogue Service

**Responsible:** [Ashish Kumar Singh]

Handles menus and food items.

**Owns:** Menus, Categories, Food Items

### Order Service

**Responsible:** [Abhishek Kumar Jana]

Handles carts and food orders.

**Owns:** Carts, Cart Items, Orders, Order Items

### Payment Service

**Responsible:** [Tushar Bharadwaj]

Handles payments for orders.

**Owns:** Payments

### User & Admin Service

**Responsible:** [Bikash Pradhan]

Handles users and vendors.

**Owns:** Users, Vendors

### Service Communication

| Caller Service | Target Service | Operation      |
| -------------- | -------------- | -------------- |
| Order          | Catalogue      | checkItem      |
| Order          | Catalogue      | getMenu        |
| Order          | Payment        | processPayment |
| Order          | User & Admin   | getVendor      |

Services communicate through defined operations and do not directly access another service's data.

## 3. Service Contracts

### Catalogue Service

| Operation  | Input        | Output                        | Errors                     |
| ---------- | ------------ | ----------------------------- | -------------------------- |
| getMenu    | Menu request | Menu items                    | Menu not found             |
| checkItem  | Food item    | Item details and availability | Item not found/unavailable |
| searchFood | Search text  | Matching items                | No results                 |

### Order Service

| Operation      | Input                 | Output              | Errors                    |
| -------------- | --------------------- | ------------------- | ------------------------- |
| addToCart      | Item, quantity        | Updated cart        | Item unavailable          |
| removeFromCart |  Item                  | Updated cart        | Item not in cart          |
| placeOrder     | Cart, payment details | Order confirmation  | Empty cart/payment failed |
| cancelOrder    | Order                 | Cancellation result | Order not found           |

### Payment Service

| Operation        | Input                   | Output         | Errors            |
| ---------------- | ----------------------- | -------------- | ----------------- |
| processPayment   | Amount, payment details | Payment result | Payment failed    |
| getPaymentStatus | Payment reference       | Payment status | Payment not found |

### User & Admin Service

| Operation  | Input          | Output         | Errors           |
| ---------- | -------------- | -------------- | ---------------- |
| getVendor  | Vendor request | Vendor details | Vendor not found |
| manageUser | User details   | Updated user   | Invalid user     |

## 4. Central Operation — placeOrder

`placeOrder` is used by a student to place an order from the items in the cart.

**Input:** Cart items and payment details.

**Output:** Order confirmation, total amount and payment status.

### Main Steps

1. Check that the cart is not empty.
2. Check that the selected food items are available.
3. Get the vendor information.
4. Process the payment.
5. Create the order and return the confirmation.

### Possible Errors

* Empty cart
* Food item unavailable
* Vendor not found
* Payment failed

The caller does not need to know how the order, payment or food data is stored internally.

## 5. Service Validation

| Service      | Reachable | Self-contained | Contract | Independent | Loosely Coupled |
| ------------ | --------- | -------------- | -------- | ----------- | --------------- |
| Catalogue    | Yes       | Yes            | Yes      | Yes         | Yes             |
| Order        | Yes       | Yes            | Yes      | Yes         | Yes             |
| Payment      | Yes       | Yes            | Yes      | Yes         | Yes             |
| User & Admin | Yes       | Yes            | Yes      | Yes         | Yes             |

The services have their own data and communicate through defined operations instead of directly accessing each other's data.
