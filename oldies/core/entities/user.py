from enum import Enum


class Role(Enum):
    ADMIN = 0
    EMPLOYEE = 1


class User:
    def __init__(self, name, first_name, password, role):
        self.name = name
        self.first_name = first_name
        self.password = password
        self.role = role
