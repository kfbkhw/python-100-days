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


def print_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if "money" in resources:
        money = resources["money"]
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"
    else:
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"


def resources_check(menu_ingredients):
    # check resources >= menu ingredients
    for item in menu_ingredients:
        if resources[item] < menu_ingredients[item]:
            # 2-1. false (not enough resources)
            print(f"Sorry, there is not enough {item}.")
            return False
    # 2-2. true (enough resources)
    print("Please insert coins.")
    return True


def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    inserted_total = (quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01)
    return inserted_total


def money_check(inserted, menu_cost, menu_ingredients, menu):
    global resources
    if menu_cost > inserted:
        # 4-1. not enough money
        print("Sorry, that's not enough money. Money refunded.")
    else:
        # 4-2. enough money
        if "money" in resources:
            resources["money"] += menu_cost
        else:
            resources["money"] = menu_cost
        if inserted > menu_cost:
            change = round((inserted - menu_cost), 2)
            print(f"Here is ${change} in change.")
        for item in menu_ingredients:
            resources[item] -= menu_ingredients[item]
        print(f"Here is your {menu} ☕️. Enjoy!")


# 0. variable "status" on/off
status = "on"
# 0-1. continue running while on
while status == "on":
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # 0-2. "off"
    if response == "off":
        status = "off"
    # 1. "report"
    elif response == "report":
        print(print_resources())
    # 2. one of the menus
    else:
        if resources_check(MENU[response]["ingredients"]):
            # 3. calculate the inserted coins using a function
            total = insert_coins()
            # 4. check inserted coins > menu cost
            money_check(total, MENU[response]["cost"], MENU[response]["ingredients"], response)
