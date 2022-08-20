from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power = "on"
menu = Menu()
machine = CoffeeMaker()
moneyprocces = MoneyMachine()
while power == "on":
    order_name = input(f"What would you like? {menu.get_items()}: ")
    if order_name == "off":
        power = "off"
    elif order_name == "report":
        machine.report()
        moneyprocces.report()
    else:
        item = menu.find_drink(order_name)
        if machine.is_resource_sufficient(item):
            if moneyprocces.make_payment(item.cost):
                machine.make_coffee(item)
