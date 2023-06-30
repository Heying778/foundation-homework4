class InsufficientFundsError(Exception):
    pass


def simulate_shop():
    items = {
        "aPPlE": 50,
        "bAnaNa": 75,
        "laPtoP": 150
    }

    customer_balance = 100

    print("Welcome to the shop!")
    print("Here are the available items and their prices:")
    for item, price in items.items():
        print(f"{item}: £{price}")
    print("Type 'exit' to leave the shop.")

    try:
        for _ in range(3):
            option = input("Enter the item you want to purchase: ")

            if option == "exit":
                print("Thank you for visiting the shop!")
                return

            if option not in items:
                raise ValueError("Invalid input! Please select a valid item.")

            price = items[option]

            if price > customer_balance:
                raise InsufficientFundsError("You don't have enough money to purchase this item.")

            customer_balance -= price
            print(f"Here's your {option}!")

    except InsufficientFundsError as e:
        print(str(e))
        response = input("Do you have more money? (yes/no): ")

        if response.lower() == "yes":
            extra_money = float(input("Enter the additional amount of money you have: "))
            customer_balance += extra_money
            print("Additional money added to your balance.")
            simulate_shop()
        else:
            print("Sorry, you don't have enough money to continue shopping.")

    except ValueError as e:
        print(str(e))
        simulate_shop()

    else:
        print("You have reached the maximum number of items to purchase.")
        print("Thank you for visiting the shop!")

    finally:
        print("Exiting the shop.")


simulate_shop()
