from typing import List

from pymongo import MongoClient
from oldies.core.persistance.repos.repo_interface import IRepo
from oldies.core.entities.dish import (Dish)


class DishMongoRepo(IRepo):
    def __init__(self, uri):
        super().__init__()
        self.client = MongoClient(uri)
        self.db = self.client["OldiesApahida"]
        self.dishes = self.db["dishes"]

    def find(self, query):
        dish_record = self.dishes.find(query)
        try:
            dish_record = dish_record[0]
            return Dish(
                name=dish_record["name"],
                price=dish_record["price"],
                stock=dish_record["stock"],
            )
        except:
            return None

    def list(self) -> List[Dish]:
        dishes = []
        dish_records = self.dishes.find({})
        for dish_record in dish_records:
            dishes.append(
                Dish(
                    name=dish_record["name"],
                    price=dish_record["price"],
                    stock=dish_record["stock"],
                )
            )
        return dishes

    def insert(self, dish: Dish):
        self.dishes.insert_one({
            "name": dish.name,
            "price": dish.price,
            "stock": dish.stock,
        })

    def update(self, dish_id, dish: Dish):
        self.dishes.update_one(
            {"_id": dish_id},
            {
                "name": dish.name,
                "price": dish.price,
                "stock": dish.stock,
            }
        )

    def delete(self, dish_id):
        self.dishes.delete_one({"_id": dish_id})
