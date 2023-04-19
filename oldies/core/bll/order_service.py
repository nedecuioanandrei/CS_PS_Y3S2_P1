from oldies.core.entities.order import Order
from typing import List


class OrderService:
    def __init__(self, order_repo):
        self.order_repo = order_repo

    def add_order(self, order):
        return self.order_repo.insert(order)

    def _check_stock(self):
        pass

    def update_status(self, order_id):
        pass

    def list(self) -> List[Order]:
        return self.order_repo.list()

    def generate_report(self, time_interval, export_format):
        pass
