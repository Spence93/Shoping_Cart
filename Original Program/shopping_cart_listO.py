items = ["Whiskers", "Kong", "Hay", "Fish Food"]
prices = [5, 3, 15, 2]
item_price = []
cart = []

item_count = 0

program = False

# variables created for later addition of Quantiy change items in the basket
whiskers = 0
kong = 0
hay = 0
fish = 0

# Start of program and inital menu for user to see
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
    # An IF statement to display the users shopping cart if there are items
    # in their cart
    if (len(cart) > 0):
        end = False
        counter = 0
        while (not end):

            if (counter == len(cart)-1):
                end = True

            print(f" {cart[counter]}, £{item_price[counter]}")
            counter += 1
    # Main menu for the program
    print("-" * 75)
    print("1. Add an item to your cart")
    print("2. Remove an item to your cart")
    print("3. View total cost")
    print("4. Checkout")
    print("-" * 75)
    menu_choice = int(input("Please enter the number of your menu choice: "))
    print("-" * 75)

    # IF-ELSE statements, to take the users previous input-
    # choice 1 is to add item to their cart
    if menu_choice == 1:
        print("Please choose which item you want to add: ")
        print(""" 1. Whiskers Cat Food \n 2. Kong Dog Food\n 3. Hay\n 4. Fish Food
              """)
        item_choice = int(
            input("Please type the item from the list you wish to add: "))
        print("-" * 75)

        # A for loop to take users input for item_choice and iterate through
        # the original item list, and add correct item
        for i in range(5):
            if item_choice == i:
                cart.append(items[i-1])
                item_count += 1

                # If-else statements to determine which item price should
                # be added in addition ot the item
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
    # Second menu choice, this will allow them to remove an item.
    if menu_choice == 2:
        print(" Please choose which item you want to remove: ")
        print(""" 1. Whiskers \n 2. Kong \n 3. Hay \n 4. Fish Food""")
        item_remove = int(input(" Please choose an option to remove: "))
        print("-" * 75)

        # A for loop to create list indexes to allow us to remove the users
        # selected item
        for x in range(5):
            if item_remove == x:
                cart.remove(items[x-1])
                item_count -= 1

                # If-Else statements to also remove the users chosen
                # items price from the corresonding list
                if item_remove == 1:
                    print(""" \n You have removed 1x Whiskers""")
                    whiskers -= 1
                    item_price.remove(5)
                elif item_remove == 2:
                    print("""You have removed 1x Kong""")
                    kong -= 1
                    item_price.remove(3)
                elif item_remove == 3:
                    print("""You have removed 1x Hay""")
                    hay -= 1
                    item_price.remove(15)
                elif item_remove == 4:
                    print("""You have removed 1x Fish Food""")
                    fish -= 1
                    item_price.remove(2)

    # Third menu choice, which will display the users cart and
    # calculate the total price
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

        print("-" * 75)
        print(f" Total price: £{total_price}")
        print("-" * 75)
        # Gives the user the option to end program after viewing cart and
        # price, or to continue
        print("1. Yes")
        print("2. No")
        pay = int(input("Would you like to checkout? "))
        if pay == 1:
            program = True

    # Fourth menu choice, allows the user to end the program
    elif menu_choice == 4:
        program = True
        print("done")
