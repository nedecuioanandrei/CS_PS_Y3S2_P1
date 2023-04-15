import hashlib
from oldies.core.entities.user import User


class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    @staticmethod
    def _encrypt_password(password):
        return hashlib.shake_256(bytes(password, "utf-8"))

    def login(self, username, password) -> User:
        pass


