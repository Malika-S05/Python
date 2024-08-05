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
profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 500,
}


def is_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print("Sorry there is not enough water.")
            return False
    else:
        return True


def get_report():
    print(f"""
    Water: {resources.get("water")}ml
    Milk: {resources.get("milk")}ml
    Coffee:{resources.get("coffee")}g
    Money: ${profit}""")


def process_coins():
    print("Please insert coins.")
    amt = int(input("how many quarters?:")) * .25
    amt += int(input("how many dimes?:")) * .10
    amt += int(input("how many nickles?:")) * .05
    amt += int(input("how many pennies?:")) * .01
    return amt


def transaction_suscessful(amt,ordered):
    if amt < MENU[ordered]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += MENU[ordered]["cost"]
        change = amt - MENU[ordered]["cost"]
        print(f"Here is ${(round(change, 2))}dollars in change.")
        return True

def make_coffee(order):
    resources["water"] -= MENU[order]["ingredients"]["water"]
    if order != "espresso":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    print(f"Here is your {order}☕.Enjoy!.")


is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino) :")
    if order.lower() == "report":
        get_report()
    elif order.lower() == "off":
        is_on = False
    else:
        if is_sufficient(MENU[order]["ingredients"]):
            amt1 = process_coins()
            if transaction_suscessful(amt1,order):
                make_coffee(order)





