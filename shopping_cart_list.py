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
        # while (not end):

        #     if (counter == len(cart)-1):
        #         end = True

        #     print(f" {cart[counter]}, £{item_price[counter]}") # needs changing
        #     counter += 1

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

        for i in range(5):  # changed from range 5
            if items[i-1] not in cart:

                if item_choice == i:
                    cart.append(items[i-1])
                    item_count += 1

                    if item_choice == 1:
                        print("You have added 1x Whiskers")
                        whiskers += 1
                        items[0][1] = whiskers
                        break
                    elif item_choice == 2:
                        print("You have added 1x Kong")
                        kong += 1
                        items[1][1] = kong
                        break
                    elif item_choice == 3:
                        print("You have added 1x Hay")
                        hay += 1
                        items[2][1] = hay

                    elif item_choice == 4:
                        print("You have added 1x Fish Food")
                        fish += 1
                        items[3][1] = fish

            elif items[0] in cart and item_choice == 1:
                for x in cart:
                    if items[0][0] in x:  # if whiskers in cart
                        index_1 = cart.index(x)
                        index_2 = x.index("Whiskers")
                        cart[index_1][index_2 + 1] += 1
                        break
                break
            elif items[1] in cart and item_choice == 2:
                for x in cart:
                    if items[1][0] in x:  # if Kong in cart
                        index_1 = cart.index(x)
                        index_2 = x.index("Kong")
                        cart[index_1][index_2 + 1] += 1
                        break
                break
            elif items[2] in cart and item_choice == 3:
                for x in cart:
                    if items[2][0] in x:  # if Kong in cart
                        index_1 = cart.index(x)
                        index_2 = x.index("Hay")
                        cart[index_1][index_2 + 1] += 1
                        break
                break
            elif items[3] in cart and item_choice == 4:
                for x in cart:
                    if items[3][0] in x:  # if Kong in cart
                        index_1 = cart.index(x)
                        index_2 = x.index("Fish Food")
                        cart[index_1][index_2 + 1] += 1
                        break
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
