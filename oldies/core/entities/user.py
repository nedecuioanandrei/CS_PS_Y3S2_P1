from enum import Enum


class Role(Enum):
    ADMIN = 0
    EMPLOYEE = 1

    def __str__(self):
        if self.ADMIN == self:
            return "admin"
        else:
            return "employee"


class User:
    def __init__(self, name, first_name, username, password, role):
        self.name = name
        self.first_name = first_name
        self.username = username
        self.password = password
        self.role = role

    def as_tuple(self):
        return self.name, self.first_name, self.username, self.role, self.password

    def __str__(self):
        return f"Name: {self.name}\nFirstname: {self.first_name}\nUsername: {self.username}\nRole: {self.role}\n"
