logo = """
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
"""

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
}

coffee_machine_running = True
money = 0


def resource():
    print("Current resources: ")
    print(f"  Water: {resources['water']}ml")
    print(f"  Milk: {resources['milk']}ml")
    print(f"  Coffee: {resources['coffee']}g")
    print(f"  Money: ${money}")


def check_espresso():
    if (MENU['espresso']['ingredients']['water']) <= resources['water'] and (
            MENU['espresso']['ingredients']['coffee']) <= resources['coffee']:
        return True
    else:
        return False


def out_of_espresso():
    if (MENU['espresso']['ingredients']['water']) > resources['water']:
        return "Sorry, there is not enough water."
    elif (MENU['espresso']['ingredients']['coffee']) > resources['coffee']:
        return "Sorry, there is not enough coffee."
    else:
        return "Sorry, there is not enough water and coffee."


def check_latte():
    if (MENU['latte']['ingredients']['water']) <= resources['water'] and (
            MENU['latte']['ingredients']['milk']) <= resources['milk'] and (
            MENU['latte']['ingredients']['coffee']) <= resources['coffee']:
        return True
    else:
        return False


def out_of_latte():
    if (MENU['latte']['ingredients']['water']) > resources['water'] and (MENU['latte']['ingredients']['milk']) > \
            resources['milk']:
        return "Sorry, there is not enough water and milk."
    elif (MENU['latte']['ingredients']['water']) > resources['water'] and (MENU['latte']['ingredients']['coffee']) > \
            resources['coffee']:
        return "Sorry, there is not enough water and coffee."
    elif (MENU['latte']['ingredients']['milk']) > resources['milk'] and (MENU['latte']['ingredients']['coffee']) > \
            resources['coffee']:
        return "Sorry, there is not enough milk and coffee."
    elif (MENU['latte']['ingredients']['water']) > resources['water']:
        return "Sorry, there is not enough water."
    elif (MENU['latte']['ingredients']['milk']) > resources['milk']:
        return "Sorry, there is not enough milk."
    elif (MENU['latte']['ingredients']['coffee']) > resources['coffee']:
        return "Sorry, there is not enough coffee."
    else:
        return "Sorry, there is not enough water, milk, and coffee."


def check_cappuccino():
    if (MENU['cappuccino']['ingredients']['water']) <= resources['water'] and (
            MENU['cappuccino']['ingredients']['milk']) <= resources['milk'] and (
            MENU['cappuccino']['ingredients']['coffee']) <= resources['coffee']:
        return True
    else:
        return False


def out_of_cappuccino():
    if (MENU['cappuccino']['ingredients']['water']) > resources['water'] and (
            MENU['cappuccino']['ingredients']['milk']) > resources['milk']:
        return "Sorry, there is not enough water and milk."
    elif (MENU['cappuccino']['ingredients']['water']) > resources['water'] and (
            MENU['cappuccino']['ingredients']['coffee']) > resources['coffee']:
        return "Sorry, there is not enough water and coffee."
    elif (MENU['cappuccino']['ingredients']['milk']) > resources['milk'] and (
            MENU['cappuccino']['ingredients']['coffee']) > resources['coffee']:
        return "Sorry, there is not enough milk and coffee."
    elif (MENU['cappuccino']['ingredients']['water']) > resources['water']:
        return "Sorry, there is not enough water."
    elif (MENU['cappuccino']['ingredients']['milk']) > resources['milk']:
        return "Sorry, there is not enough milk."
    elif (MENU['cappuccino']['ingredients']['coffee']) > resources['coffee']:
        return "Sorry, there is not enough coffee."
    else:
        return "Sorry, there is not enough water, milk, and coffee."


def get_coins(choice):
    print("Please insert coins: ")
    quarters = int(input("  How many quarters? "))
    total_quarters = quarters * 0.25
    dimes = int(input("  How many dimes? "))
    total_dimes = dimes * 0.1
    nickles = int(input("  How many nickles? "))
    total_nickles = nickles * 0.05
    pennies = int(input("  How many pennies? "))
    total_pennies = pennies * 0.01
    total = total_quarters + total_dimes + total_nickles + total_pennies
    return total


def enough_coins(amount, choice):
    if amount >= MENU[choice]['cost']:
        return True
    else:
        return False


def resource_usage(choice):
    if choice == 'espresso':
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']


print("Welcome to your virtual coffee machine! ")
print(logo)

while coffee_machine_running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == 'espresso':
        if check_espresso():
            print("  You chose espresso. This costs $1.50")
            coins = get_coins(user_input)
            if enough_coins(coins, user_input):
                money += MENU[user_input]['cost']
                change = coins - MENU[user_input]['cost']
                resource_usage(user_input)
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                print("Here is your espresso ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(out_of_espresso())

    elif user_input == 'latte':
        if check_latte():
            print("  You chose latte. This costs $2.50")
            coins = get_coins(user_input)
            if enough_coins(coins, user_input):
                money += MENU[user_input]['cost']
                change = coins - MENU[user_input]['cost']
                resource_usage(user_input)
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                print("Here is your latte ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(out_of_latte())

    elif user_input == 'cappuccino':
        if check_cappuccino():
            print("  You chose cappuccino. This costs $3.00")
            coins = get_coins(user_input)
            if enough_coins(coins, user_input):
                money += MENU[user_input]['cost']
                change = coins - MENU[user_input]['cost']
                resource_usage(user_input)
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change.")
                print("Here is your cappuccino ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(out_of_cappuccino())

    elif user_input == 'report':
        # print current resources
        resource()

    elif user_input == 'off':
        # end execution of coffee machine
        print("Turning off coffee machine. ")
        coffee_machine_running = False

    else:
        print("Invalid input. Try again.")