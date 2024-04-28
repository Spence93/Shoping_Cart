# from paws_and_cart_MAIN import stock_file


class Cart:
    def __init__(self) -> None:
        self.cart = []

    def get_cart(self):

        for item in (self.cart):
            print(
                f"{item.quantity}x {item.name}   -   £{item.price}")

    def add_item(self, stock, index):
        if index.isdigit():
            index = int(index) - 1
            if index >= 0 and (index) <= len(stock.stock_list):
                if stock.stock_list[index] not in self.cart:
                    self.cart.append(stock.stock_list[index])
                    self.cart[-1].quantity += 1
                    self.cart[-1].stock_level -= 1
                    print(f"1x {self.cart[-1].name} added to your cart!")

                else:
                    for item in self.cart:
                        if stock.stock_list[index].name == item.name:
                            item.quantity += 1
                            item.stock_level -= 1

            else:
                print("Not a valid choice")

    def remove_item(self):
        pass

    def total_price(self):
        pass
