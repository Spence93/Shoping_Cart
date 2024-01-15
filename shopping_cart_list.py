items = [["Whiskers", 0, 5],
         ["Kong", 0, 3],
         ["Hay", 0, 15],
         ["Fish Food", 0, 2]]

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
    print("-" * 75)
    print("1. Add an item to your cart")
    print("2. Remove an item to your cart")
    print("3. View total cost")
    print("4. Checkout")
    print("-" * 75)
    menu_choice = int(input("Please enter the number of your menu choice: "))
    print("-" * 75)

    # Adding items to the user scart
    if menu_choice == 1:
        print("Please choose which item you want to add: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")

        item_choice = int(
            input("Please type the item from the list you wish to add: "))

        for i in range(len(items)):  # changed from below "Old code" Works!
            if items[i] not in cart:
                if item_choice == i+1:
                    cart.append(items[i])
                    print(f"You have added 1x {items[i][0]}")
                    if items[i][0] == cart[-1][0]:
                        cart[-1][1] += 1
                        item_count += 1
                        break


# doesnt work yet - need conditonal to seperate this
            elif items[i] in cart and item_choice == i+1:

                # for y in range(len(items)):
                #     if cart[y][1] > 0:

                for x in cart:
                    if item_choice == i + 1:
                        if items[i] == x:
                            index_1 = cart.index(x)
                            cart[index_1][1] += 1
                            item_count += 1
                            break

    if menu_choice == 2:
        print(" Please choose which item you want to remove: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")

        # item_remove = int(input(" Please choose an option to remove: "))
        # for x in range(5):
        #     if item_remove == x:
        #         cart.remove(items[x-1])
        #         item_count -= 1
        #         if item_remove == 1:
        #             print("You have removed 1x Whiskers")
        #             whiskers -= 1
        #             item_price.remove(5)
        #         elif item_remove == 2:
        #             print("You have removed 1x Kong")
        #             kong -= 1
        #             item_price.remove(3)
        #         elif item_remove == 3:
        #             print("You have removed 1x Hay")
        #             hay -= 1
        #             item_price.remove(15)
        #         elif item_remove == 4:
        #             print("You have removed 1x Fish Food")
        #             fish -= 1
        #             item_price.remove(2)
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
