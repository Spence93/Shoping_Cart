class Items:

    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        print(f"\n{self.name}\t{self.price}")
