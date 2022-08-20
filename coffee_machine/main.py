# coffee machine
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
    "money": 0,
}


def money(selection):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_inserted = 0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
    if total_inserted < MENU[selection]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total_inserted - MENU[selection]["cost"]
        if change != 0:
            print(f"Here is ${change} in change.")
        resources["money"] += MENU[selection]["cost"]
        return True


def prepare(selection):
    if selection == "espresso":
        if resources["water"] >= MENU[selection]["ingredients"]["water"] and resources["coffee"] >= MENU[selection]["ingredients"]["coffee"]:
            resources["water"] = resources["water"] - \
                MENU[selection]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - \
                MENU[selection]["ingredients"]["coffee"]
            check_money = money(selection)
            if check_money:
                print(f"Here is your {selection} ☕️. Enjoy!")
        elif resources["water"] < MENU[selection]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU[selection]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Sorry smthing went wrong")
    if selection == "latte" or selection == "cappuccino":
        if resources["water"] >= MENU[selection]["ingredients"]["water"] and resources["coffee"] >= MENU[selection]["ingredients"]["coffee"] and resources["milk"] >= MENU[selection]["ingredients"]["milk"]:
            resources["water"] = resources["water"] - \
                MENU[selection]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - \
                MENU[selection]["ingredients"]["coffee"]
            check_money = money(selection)
            if check_money:
                print(f"Here is your {selection} ☕️. Enjoy!")
        elif resources["water"] < MENU[selection]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU[selection]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        elif resources["milk"] < MENU[selection]["ingredients"]["milk"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Sorry smthing went wrong")


power = "on"

while power == "on":
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "off":
        power = "off"
    elif selection == "report":
        for resource in resources:
            if resource == "water" or resource == "milk":
                print(f"{resource.title()} {resources[resource]}ml")
            elif resource == "money":
                print(f"{resource.title()} ${resources[resource]}")
            else:
                print(f"{resource.title()} {resources[resource]}g")
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        prepare(selection)
    else:
        print("Wrong selection")
