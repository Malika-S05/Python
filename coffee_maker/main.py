from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()
is_on = True
while is_on == True:
    choice = input(f"What would you like to have?({menu.get_items()}): ")
    if choice == "report":
        coffee_maker.report()
        my_money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item):
            if my_money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)






