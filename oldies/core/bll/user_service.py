import hashlib
from oldies.core.entities.user import (Role, User)


class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    @staticmethod
    def _encrypt_password(password):
        return hashlib.sha256(bytes(password, "utf-8")).hexdigest()

    def login(self, username, password) -> User:
        return self.user_repo.find(username, self._encrypt_password(password))

    def create_user(self, user: User, password):
        return self.user_repo.insert(user, self._encrypt_password(password))


    def list(self):
        return self.user_repo.list()
