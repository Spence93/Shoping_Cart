# from paws_and_cart_MAIN import stock_file


class Cart:
    def __init__(self) -> None:
        self.cart = []
        self.whiskers = 0
        self.kong = 0
        self.hay = 0
        self.fish_food = 0

    # def get_cart(self):
    #     for item in self.cart:
    #         if item.name == "Whiskers":
    #             self.whiskers += 1
    #         elif item.name == "Kong":
    #             self.kong += 1
    #         elif item.name == "Hay":
    #             self.hay += 1
    #         elif item.name == "Fish Food":
    #             self.fish_food += 1

    def add_item(self, stock, index):
        if index.isdigit():
            index = int(index) - 1
            if index >= 0 and (index) <= len(stock.stock_list):
                self.cart.append(stock.stock_list[index])
                print(f"1x {self.cart[-1].name} added to cart!")

            else:
                print("Not a valid choice")

    def remove_item(self):
        pass

    def total_price(self):
        pass
