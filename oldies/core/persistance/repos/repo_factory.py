from oldies.core.persistance.mongo.user_mongo_repo import UserMongoRepo
from oldies.core.persistance.repos.repo_interface import IRepo


class RepoFactory:
    def __init__(self, context):
        self.context = context

    def get_user_repo(self) -> IRepo:
        if self.context["db"] == "mongo":
            return UserMongoRepo(uri=self.context["database_uri"])

    def get_account_repo(self):
        pass

    def get_order_repo(self):
        pass

    def get_menu_repo(self):
        pass
