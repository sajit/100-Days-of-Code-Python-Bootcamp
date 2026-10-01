from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

shop_menu = Menu()
coffee_maker = CoffeeMaker()
kiosk = MoneyMachine()


def is_valid_item(item):
    return item in shop_menu.get_items().split("/")

user_choice = input(" What would you like? (espresso/latte/cappuccino):")
while user_choice != "off":
    if is_valid_item(user_choice):
        drink = shop_menu.find_drink(user_choice)
        print(f"You chose {user_choice}. It costs {drink.cost}.")     
        if coffee_maker.is_resource_sufficient(drink):
             if kiosk.make_payment(drink.cost):
                 coffee_maker.make_coffee(drink)
             else:
                 print(f"Not enough money to process transactions")
        else:
            print(f"Not enough ingredients to make {user_choice}. ")
                     
    elif user_choice == "report":
        coffee_maker.report()
        kiosk.report()
    else:
        print("Enter valid item. Off to end. Report to generate report")
    user_choice = input(" What would you like? (espresso/latte/cappuccino):")