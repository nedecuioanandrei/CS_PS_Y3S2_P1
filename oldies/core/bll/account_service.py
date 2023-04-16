from oldies.core.entities.user import (Role, User)


class AccountService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def create_account(self, name, username, password):
        pass
