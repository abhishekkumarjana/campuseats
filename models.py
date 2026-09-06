class Order:
    def __init__(
        self,
        order_id,
        student_id,
        items,
        delivery_address_id,
        payment_method_id,
        status="CREATED",
        total=0.0,
        idempotency_key=None
    ):
        self.order_id = order_id
        self.student_id = student_id
        self.items = items
        self.delivery_address_id = delivery_address_id
        self.payment_method_id = payment_method_id
        self.status = status
        self.total = total
        self.idempotency_key = idempotency_key

    def as_json(self):
        return {
            "orderId": self.order_id,
            "studentId": self.student_id,
            "items": self.items,
            "deliveryAddressId": self.delivery_address_id,
            "status": self.status,
            "total": self.total
        }