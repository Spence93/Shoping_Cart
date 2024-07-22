import copy

stock_file = [["Whiskers", 0, 5],
              ["Kong", 0, 3],
              ["Hay", 0, 15],
              ["Fish Food", 0, 2]]

items = copy.deepcopy(stock_file)

cart = []

item_count = 0
total_price = 0
program = False
end = False


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
        # print("\n")
    print("-" * 75)
    print("This is your Shopping Cart: ")
    if len(cart) > 0:
        counter = 0
        end = False
        while (not end):
            if (counter == len(cart)-1):
                end = True

            print(f" {cart[counter][1]}x {cart[counter][0]\
                                          } - £{cart[counter][1] * cart[counter][2]}")
            counter += 1
    print("-" * 75)
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View total cost")
    print("4. Checkout")
    print("-" * 75)
    menu_choice = int(input("Please choose a number from the menu: "))
    print("-" * 75)

    # Adding items to the users cart
    if menu_choice == 1:
        print("Please choose which item you want to add: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")

        item_choice = int(input("Please choose a number from the menu: "))

        for i in range(len(items)):  # changed from below "Old code" Works!
            if items[i] not in cart:
                if item_choice == i+1:
                    cart.append(items[i])
                    print("-" * 75)
                    print(f"You have added 1x {items[i][0]} - £{items[i][2]}")
                    print("-" * 75)
                    if items[i][0] == cart[-1][0]:
                        cart[-1][1] += 1
                        item_count += 1
                        break


# If the item is in the users cart, this code excecutes to update the quantity

            elif items[i] in cart and item_choice == i+1:
                for x in cart:
                    if item_choice == i + 1:
                        if items[i] == x:
                            index_1 = cart.index(x)
                            cart[index_1][1] += 1
                            print("-" * 75)
                            print(f"You have added 1x {\
                                  items[i][0]} - £{items[i][2]}")
                            print("-" * 75)
                            item_count += 1
                            break

    if menu_choice == 2:
        print(" Please choose which item you want to remove: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")

        item_remove = int(input(" Please choose an option to remove: "))

        for i in range(len(items)):
            for x in cart:  # changed from below "Old code" Works!
                if items[i] in cart and item_remove == i + 1:
                    if items[i] == x:
                        index_2 = cart.index(x)
                        cart[index_2][1] -= 1
                        print("-" * 75)
                        print(f"You removed 1x {cart[index_2][0]}")
                        print("-" * 75)
                        if cart[index_2][1] == 0:
                            cart.remove(cart[index_2])
                            break
                        break

    elif menu_choice == 3:
        print("Your Cart: ")
        for i in range(len(cart)):
            total_price += cart[i][1] * cart[i][2]

        counter = 0
        end = False
        while (not end):
            if (counter == len(cart)-1):
                end = True

            print(f" {cart[counter][1]}x {cart[counter][0]\
                                          } - £{cart[counter][1] * cart[counter][2]}")
            counter += 1
        print("-" * 19)
        print(f" Total price: £{total_price}")
        print("-" * 75)
        print("1. Yes")
        print("2. No")
        pay = int(input("Would you like to continue to checkout? "))
        if pay == 1:
            program = True

    elif menu_choice == 4:
        program = True
        print("done")
