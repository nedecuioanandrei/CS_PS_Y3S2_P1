from pymongo import MongoClient

class UserMongoDa:
    def __init__(self):
        self.client = MongoClient("mongodb://root:hello@localhost:27017/")
        self.db = self.client["OldiesApahida"]
        self.users = self.db["users"]

    def find_one(self):
        return self.users.find()

    def find_by_id(self, user_id):
        return self.users.find({"_id": user_id})


import pprint as pp
c = UserMongoDa()
f = c.find_one()

for b in f:
    pp.pprint(b)
# f = c.find_by_id("643b139588d73da33ffe7785")