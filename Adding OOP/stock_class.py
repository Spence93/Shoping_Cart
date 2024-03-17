from items_class import Items
import os


class Stock:

    def __init__(self) -> None:
        self.stock_list = []

    def add_stock(self, stock):
        with open(stock, "r") as file:
            stock_file = []

            for x in file.readlines():
                temp = (x.strip("\n").strip("").split(","))
                stock_file.append(temp)

            for item in (stock_file):
                product = (Items(item[0], item[1], item[2]))
                self.stock_list.append(product)

    def get_stock(self):
        for i, item in enumerate(self.stock_list, 1):
            print(f"{i}. {item.name}  \t- £{item.price}")
