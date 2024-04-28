class Items:

    def __init__(self, name, stock_level, quantity, price) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.stock_level = stock_level

    def __str__(self):
        print(f"\n{self.name}\t{self.price}")
