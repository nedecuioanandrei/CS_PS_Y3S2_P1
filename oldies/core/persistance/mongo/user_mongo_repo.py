from typing import List

from pymongo import MongoClient
from oldies.core.persistance.repos.repo_interface import IRepo
from oldies.core.entities.user import (Role, User)


class UserMongoRepo(IRepo):
    def __init__(self, uri):
        super().__init__()
        self.client = MongoClient(uri)
        self.db = self.client["OldiesApahida"]
        self.users = self.db["users"]

    def find(self, user_id):
        user_record = self.users.find({"_id": user_id})
        try:
            user_record = user_record[0]
            return User(
                name=user_record["name"],
                first_name=user_record["first_name"],
                username=user_record["username"],
                password=None,
                role=Role.ADMIN if user_record["role"] == "admin" else Role.EMPLOYEE,
            )
        except:
            return None

    def find(self, username, pass_sha256) -> User:
        user_record = self.users.find({"username": username, "pass_sha256": pass_sha256})
        try:
            user_record = user_record[0]
            return User(
                name=user_record["name"],
                first_name=user_record["first_name"],
                username=user_record["username"],
                password=None,
                role=Role.ADMIN if user_record["role"] == "admin" else Role.EMPLOYEE,
            )
        except:
            return None

    def list(self) -> List[User]:
        users = []
        user_records = self.users.find({})
        for user_record in user_records:
            users.append(
                User(
                    name=user_record["name"],
                    first_name=user_record["first_name"],
                    username=user_record["username"],
                    password=None,
                    role=Role.ADMIN if user_record["role"] == "admin" else Role.EMPLOYEE,
                )
            )
        return users

    def insert(self, user: User):
        self.users.insert_one({
            "name": user.name,
            "first_name": user.first_name,
            "username": user.username,
            "password": user.password,
            "role": "admin" if user.role == Role.ADMIN else "employee"
        })

    def update(self, user_id, user: User):
        self.users.update_one(
            {"_id": user_id},
            {
                "name": user.name,
                "first_name": user.first_name,
                "username": user.username,
                "password": user.password,
                "role": "admin" if user.role == Role.ADMIN else "employee"
            }
        )

    def delete(self, user_id):
        self.users.delete_one({"_id": user_id})
