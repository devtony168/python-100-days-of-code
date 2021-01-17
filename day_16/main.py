from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_items = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_is_on = True

while coffee_machine_is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("Coffee machine turns off.")
        coffee_machine_is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
