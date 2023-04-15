from datetime import datetime
from enum import Enum


class Status(Enum):
    NEW = 1
    PREPARED = 2
    FINISHED = 3


class Order:
    def __init__(self, dish_list):
        self.dish_list = dish_list
        self.status = Status.NEW
        self.timestamp = datetime.now()
