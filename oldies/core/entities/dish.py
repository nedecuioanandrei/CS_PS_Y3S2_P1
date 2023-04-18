class Dish:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def as_tuple(self):
        return self.name, self.price, self.stock
