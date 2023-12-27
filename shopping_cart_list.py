items = ["Whiskers", "Kong", "Hay", "Fish Food"]
prices = [5, 3, 15, 2]
item_price = []
cart = []

item_count = 0

program = False


whiskers = 0
kong = 0
hay = 0
fish = 0

while (not program):
    print("\n")
    if len(cart) <= 0:
        print("-" * 75)
        print("Welcome to Paws n Cart! ")
        print("""───────────────────────────────────────
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
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────""")
        print("\n")
    print("-" * 75)
    print("This is your Shopping Cart: ")

    if (len(cart) > 0):
        # if whiskers > 1:
        #     cart.remove(items[0])

        # elif kong > 1:
        #     cart.remove(items[1])

        # elif hay > 1:
        #     cart.remove(items[2])

        # elif fish > 1:
        #     cart.remove(items[3])
        end = False
        counter = 0
        while (not end):

            if (counter == len(cart)-1):
                end = True

            print(f" {cart[counter]}, £{item_price[counter]}")
            counter += 1

    print("-" * 75)
    print("1. Add an item to your cart")
    print("2. Remove an item to your cart")
    print("3. View total cost")
    print("4. Checkout")
    print("-" * 75)
    menu_choice = int(input("Please enter the number of your menu choice: "))
    print("-" * 75)

#     # ACTIVE
    if menu_choice == 1:
        print("Please choose which item you want to add: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")

        item_choice = int(
            input("Please type the item from the list you wish to add: "))

        for i in range(5):
            if item_choice == i:
                cart.append(items[i-1])
                item_count += 1
                if item_choice == 1:
                    print("You have added 1x Whiskers")
                    whiskers += 1
                    item_price.append(prices[0])
                elif item_choice == 2:
                    print("You have added 1x Kong")
                    kong += 1
                    item_price.append(prices[1])
                elif item_choice == 3:
                    print("You have added 1x Hay")
                    hay += 1
                    item_price.append(prices[2])
                elif item_choice == 4:
                    print("You have added 1x Fish Food")
                    fish += 1
                    item_price.append(prices[3])

    if menu_choice == 2:
        print(" Please choose which item you want to remove: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")

        item_remove = int(input(" Please choose an option to remove: "))
        for x in range(5):
            if item_remove == x:
                cart.remove(items[x-1])
                item_count -= 1
                if item_remove == 1:
                    print("You have removed 1x Whiskers")
                    whiskers -= 1
                    item_price.remove(5)
                elif item_remove == 2:
                    print("You have removed 1x Kong")
                    kong -= 1
                    item_price.remove(3)
                elif item_remove == 3:
                    print("You have removed 1x Hay")
                    hay -= 1
                    item_price.remove(15)
                elif item_remove == 4:
                    print("You have removed 1x Fish Food")
                    fish -= 1
                    item_price.remove(2)
    elif menu_choice == 3:
        total_price = sum(item_price[:])
        print("Your cart:")
        end = False
        counter = 0
        while (not end):
            if (counter == len(cart)-1):
                end = True
            print(f" {cart[counter]}, £{item_price[counter]}")
            counter += 1
            # program = True
        print("-" * 75)
        print(f" Total price: £{total_price}")
        print("-" * 75)
        print("1. Yes")
        print("2. No")
        pay = int(input("Would you like to checkout? "))
        if pay == 1:
            program = True

    elif menu_choice == 4:
        program = True
        print("done")
