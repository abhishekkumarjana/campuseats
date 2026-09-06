class OrderStore:
    def __init__(self):
        self.orders = {}
        self.idempotency_keys = {}
        self.next_id = 1

    def create(self, order):
        order.order_id = self.next_id
        self.next_id += 1

        self.orders[order.order_id] = order

        if order.idempotency_key:
            self.idempotency_keys[order.idempotency_key] = order.order_id

        return order

    def get(self, order_id):
        return self.orders.get(order_id)

    def find_by_idempotency_key(self, key):
        order_id = self.idempotency_keys.get(key)

        if order_id is None:
            return None

        return self.orders.get(order_id)

    def list_orders(self, student_id=None, status=None):
        result = list(self.orders.values())

        if student_id:
            result = [
                order for order in result
                if order.student_id == student_id
            ]

        if status:
            result = [
                order for order in result
                if order.status == status
            ]

        return result

    def update(self, order):
        self.orders[order.order_id] = order
        return order