from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

status = "on"
menu = Menu()
machine1 = CoffeeMaker()
machine2 = MoneyMachine()

while status == "on":
    response = input(f"What would you like? ({menu.get_items()}): ").lower()
    if response == "off":
        status = "off"
    elif response == "report":
        machine1.report()
        machine2.report()
    else:
        drink = menu.find_drink(response)
        if drink:
            if machine1.is_resource_sufficient(drink):
                if machine2.make_payment(drink.cost):
                    machine1.make_coffee(drink)
