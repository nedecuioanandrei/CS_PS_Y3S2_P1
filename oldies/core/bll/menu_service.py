class MenuService:
    def __init__(self, menu_repo):
        self.menu_repo = menu_repo

    def update_price(self, dish, new_price):
        pass

    def remove_dish(self, item_id):
        pass

    def add_dish(self, name, price, quantity):
        pass

    def list(self):
        return self.menu_repo.list()
