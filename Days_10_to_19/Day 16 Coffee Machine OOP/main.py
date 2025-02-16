from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker ()
menu = Menu()

while machine_on:
    response = input("What kind of coffee would you like? (espresso/latte/cappuccino)?").lower()
    if response == 'report':
        money_machine.report()
    elif response == 'off':
        machine_on = False
    elif menu.find_drink(response):
        drink = menu.find_drink((response))
        if (coffee_maker.is_resource_sufficient(drink)):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
