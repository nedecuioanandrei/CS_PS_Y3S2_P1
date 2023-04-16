from datetime import datetime
from enum import Enum


class Status(Enum):
    NEW = 1
    PREPARED = 2
    FINISHED = 3


class Order:
    def __init__(self, dish_list, status=None, timestamp=None):
        self.dish_list = dish_list
        self.status = status or Status.NEW
        self.timestamp = timestamp or datetime.now()
