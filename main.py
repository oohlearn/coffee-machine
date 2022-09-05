MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 0,
}


def switch_off(need):
    if need == "off":
        return True
    else:
        return False


def order():
    off = False
    while not off:
        need = input("What would you like? (espresso/latte/cappuccino): ")
        if need == "off":
            break
        elif need == "report":
            print(
                f"Water: {resources['water']}ml \n"
                f"Milk: {resources['milk']}ml\n"
                f"Coffee: {resources['coffee']}g\n"
                f"Money: ${resources['money']}"
            )
        else:
            while need not in MENU:
                need = input("What would you like? (espresso/latte/cappuccino): ")
            if check_resources(need):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                total_coin = round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01), 2)
                check_paid(need, total_coin)
            else:
                print("Sorry not enough materials.")


def check_paid(need, total_coin):
    if MENU[need]["cost"] > total_coin:
        print("Sorry, that's not enough money. Money refunded")
        order()
    elif MENU[need]["cost"] < total_coin:
        change = round((total_coin - MENU[need]["cost"]), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {need}. Enjoy!")
        make_coffee(need)

    else:
        make_coffee(need)
        print(f"Here is your {need}. Enjoy!")


def check_resources(need):
    if resources["water"] >= MENU[need]["ingredients"]["water"] \
            and resources["milk"] >= MENU[need]["ingredients"]["milk"] \
            and resources["coffee"] >= MENU[need]["ingredients"]["coffee"]:
        return True
    else:
        return False


def make_coffee(need):
    for ingredient in MENU[need]["ingredients"]:
        resources[ingredient] -= MENU[need]["ingredients"][ingredient]
    # resources["water"] -= MENU[need]["ingredients"]["water"]
    # resources["milk"] -= MENU[need]["ingredients"]["milk"]
    # resources["coffee"] -= MENU[need]["ingredients"]["coffee"]
    resources["money"] += MENU[need]["cost"]
    # print(resources)


order()
