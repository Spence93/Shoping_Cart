import stock_class


class Cart:
    def __init__(self) -> None:
        self.cart = []

    def set_cart(self):
        pass

    def get_cart(self):
        pass

    def add_item(self, object, index):
        if index.isdigit():
            index = int(index) - 1
            if index >= 0 and (index) <= len(object.stock_list):
                self.cart.append(object.stock_list[index])
                print(f"1x {self.cart[index].name} added to cart!")

            else:
                print("Not a valid choice")

    def remove_item(self):
        pass

    def total_price(self):
        pass
