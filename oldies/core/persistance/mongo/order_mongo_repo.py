from typing import List

from pymongo import MongoClient
from oldies.core.persistance.repos.repo_interface import IRepo
from oldies.core.entities.order import (Order, Status)


class OrderMongoRepo(IRepo):
    def __init__(self, uri):
        super().__init__()
        self.client = MongoClient(uri)
        self.db = self.client["OldiesApahida"]
        self.orders = self.db["orders"]

    def find(self, order_id):
        order_record = self.orders.find({"_id": order_id})
        try:
            order_record = order_record[0]
            status = {}
            status["new"] = Status.NEW
            status["prepared"] = Status.PREPARED
            status["finished"] = Status.FINISHED
            return Order(
                dish_list=order_record["dish_list"],
                status=status[order_record["status"]],
                timestamp=order_record["timestamp"],
            )
        except:
            return None

    def list(self) -> List[Order]:
        orders = []
        order_records = self.orders.find({})
        status = {}
        status["new"] = Status.NEW
        status["prepared"] = Status.PREPARED
        status["finished"] = Status.FINISHED
        for order_record in order_records:
            orders.append(
                Order(
                    dish_list=order_record["dish_list"],
                    status=status[order_record["status"]],
                    timestamp=order_record["timestamp"],
                )
            )
        return orders

    def insert(self, order: Order):
        self.orders.insert_one({
            "dish_list": order.dish_list,
            "status": order.status,
            "timestamp": order.timestamp,
        })

    def update(self, order_id, order: Order):
        self.orders.update_one(
            {"_id": order_id},
            {
                "dish_list": order.dish_list,
                "status": order.status,
                "timestamp": order.timestamp,
            }
        )

    def delete(self, order_id):
        self.orders.delete_one({"_id": order_id})
