# Imports
# from items_class import Items
from cart_class import Cart
from stock_class import Stock
import os


# Global Variables
menu = "-" * 75
menu += "\nWelcome to Paws n Cart! "
menu += """\n───────────────────────────────────────
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────"""
menu += "\n" + "-" * 75


def input_valid():
    while True:
        user_input = input("-> ")
        if user_input.isdigit():
            user_input = int(user_input) - 1
            return user_input

        else:
            print("Input must be a numerical digit")


# Creating stock items from .txt file.
stock = "stock_file.txt"
stock_file = Stock()
stock_file.add_stock(stock)

# Creating shopping cart from cart class
shopping_cart = Cart()


def main():
    while True:
        # To only display while cart is empty
        if len(shopping_cart.cart) < 1:
            print(menu)
        # Displays current cart if there is an item in the cart
        else:
            shopping_cart.get_cart("Your cart: ")

        # Prints user menu
        print("-" * 75)
        print("Main menu\n")
        print("1. Add an item to your cart")
        print("2. Remove an item from your cart")
        print("3. Checkout")
        print("4. Exit")
        print("-" * 75)
        user_input = input("Please choose an option from the menu:\n -> ")

        # Adding an item to users cart
        if user_input == "1":
            # Prints out available stock
            stock_file.get_stock("\nChoose an item to add to your cart: ")
            user_input = input_valid()
            shopping_cart.add_item(stock_file, user_input)

        elif user_input == "2":
            shopping_cart.get_cart("Your cart: ")
            stock_file.get_stock("\nChoose an item to remove from your cart: ")
            user_input = input_valid()
            shopping_cart.remove_item(stock_file, user_input)

        elif user_input == "3":
            shopping_cart.checkout()
            stock_file.update_stock(stock)
            break

        elif user_input == "4":
            break

        else:
            print("Incorrect option, please choose an option from the menu")
            input("Press any key to continue")


if __name__ == "__main__":
    main()
