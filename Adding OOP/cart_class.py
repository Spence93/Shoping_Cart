# from paws_and_cart_MAIN import stock_file
import time


class Cart:
    def __init__(self) -> None:
        self.cart = []

    def get_cart(self):
        print("\nYour cart: ")
        print("-" * 75)

        for item in (self.cart):
            item_total = (item.price * item.quantity)
            print(
                f"{item.quantity}x {item.name}  \t£{item_total}")
            print("-" * 75)

    def add_item(self, stock, index):
        if index >= 0 and (index) <= len(stock.stock_list):
            if stock.stock_list[index] not in self.cart:
                self.cart.append(stock.stock_list[index])
                self.cart[-1].quantity += 1
                self.cart[-1].stock_level -= 1
                print(f"\n1x {self.cart[-1].name} added to your cart!")
                time.sleep(1)

            else:
                for item in self.cart:
                    if stock.stock_list[index].name == item.name:
                        item.quantity += 1
                        item.stock_level -= 1
                        print(f"\n1x {item.name} added to your cart!")
                        time.sleep(1)
        else:
            print("Not a valid choice")

    def remove_item(self, stock, index):
        if index >= 0 and (index) <= len(stock.stock_list):
            if stock.stock_list[index] in self.cart:
                for item in self.cart:
                    if stock.stock_list[index].name == item.name and item.quantity > 0:
                        item.quantity -= 1
                        item.stock_level += 1
                        print(f"\n1x {item.name} removed from your cart!")
                        time.sleep(1)
                        if item.quantity == 0:
                            self.cart.remove(stock.stock_list[index])

            else:
                print(
                    "You cannot remove an item that is not already in your cart")

    def total_price(self):
        pass
