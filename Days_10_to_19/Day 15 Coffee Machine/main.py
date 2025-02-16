MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0
}

currency = {
    "quarter_currency": .25,
    "dime_currency": .10,
    "nickel_currency": .05,
    "penny_currency": .01
}

continue_coffee_machine = True
quarters, dimes, nickels, pennies = 0, 0, 0, 0
monetary_value = 0


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def take_order():
    return input("What would you like? (espresso/latte/cappuccino):\n"
                 "Type 'Off' to Turn Off Coffee Machine\n"
                 "Type 'Report' for Info on Coffee Machine\n").lower()


# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.

def off():
    return False


# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens

# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def report():
    for key, value in resources.items():
        print(f"{key}: {value}")


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def is_sufficient_resources(drink):
    is_enough = True
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"\nSorry we're all out of {item}")
            return False
        else:
            print("\nGREAT NEWS, WE HAVE ENOUGH OF EVERYTHING\n")
            return True


# TODO: 5. Process coins.

# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please don't give negative amounts :<(")
        except ValueError:
            print("Bruh, You can't outsmart this...maybe you can, I've only been using the fundamentals for 10+ "
                  "projects")


def process_coins():
    print("Please insert your payment in coins! :)")
    q_coins = get_positive_int("How many quarters? ")
    d_coins = get_positive_int("How many dimes? ")
    n_coins = get_positive_int("How many nickels? ")
    p_coins = get_positive_int("How many pennies? ")

    return (q_coins * currency['quarter_currency'] +
            d_coins * currency['dime_currency'] +
            n_coins * currency['nickel_currency'] +
            p_coins * currency['penny_currency']
            )


# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# b. If the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places
def is_transaction_successful(money_given, drink):
    print(f"\nTendered amount ${money_given:.2f}")
    if money_given >= MENU[drink]["cost"]:
        change = money_given - MENU[drink]["cost"]
        print(f"Price of {drink} is: ${MENU[drink]['cost']:.2f}")
        print(f"Your change is: ${change:.2f}")
        return True
    # E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    # program should say “Sorry that's not enough money. Money refunded.”
    else:
        print(f"Sorry there is not enough money. ${money_given:.2f} Refunded")
        return False


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
def make_coffee(drink):
    global resources
    resources["water"] -= MENU[drink]['ingredients']['water']
    resources["coffee"] -= MENU[drink]['ingredients']['coffee']
    resources["milk"] -= MENU[drink]['ingredients'].get("milk", 0)
    resources["Money"] += MENU[drink]["cost"]
    print(f"\nHere is your {drink}. Enjoy!")


while continue_coffee_machine:
    order = take_order()
    if order == 'off':
        continue_coffee_machine = off()
    elif order == 'report':
        report()
    elif order in MENU:
        drink = MENU[order]
        if is_sufficient_resources(drink["ingredients"]):
            monetary_value = process_coins()
            if is_transaction_successful(monetary_value, order):
                make_coffee(order)
    else:
        print("\nSorry that's not on the menu\n")
