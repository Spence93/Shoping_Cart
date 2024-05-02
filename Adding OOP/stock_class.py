from items_class import Items


class Stock:

    def __init__(self) -> None:
        self.stock_list = []

    # Add stock from a txt file, to the stock_list list
    def add_stock(self, stock):
        with open(stock, "r") as file:
            stock_file = []

            for x in file.readlines():
                temp = (x.strip("\n").strip("").split(","))
                stock_file.append(temp)

            for item in (stock_file):
                product = (Items(item[0], int(
                    item[1]), int(item[2]), int(item[3])))
                self.stock_list.append(product)

    # Displays availiable stock which has been taken from the txt file and added to the stock list class
    # **Would like to change this to use tabulate and print out current stock levels**
    def get_stock(self, prompt):
        print(prompt)
        for i, item in enumerate(self.stock_list, 1):
            print(f"{i}. {item.name}  \t- £{item.price}")

    # Update txt file with current stock quanitites after checkout
    def update_stock(self, stock):
        with open(stock, "w") as file:
            for item in self.stock_list:
                file.write(f"""{item.name}, {item.price}, 0 , {
                           item.stock_level}\n""")
