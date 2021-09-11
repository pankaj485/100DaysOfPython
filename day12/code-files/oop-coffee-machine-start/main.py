from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# print report,
# check resources is sufficient,
# process coins,
# check transaction successful,
# make coffee


is_on = True

while is_on:
    items = menu.get_items()
    user_input = input(f"what would you like to have? {items} ")

    if user_input == "off":
        is_on = False

    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_input)
        if drink:
            is_available = coffee_maker.is_resource_sufficient(drink)
            if is_available:
                process_money = money_machine.make_payment(drink.cost)
                if process_money:
                    coffee_maker.make_coffee(drink)
            else:
                is_on: False
