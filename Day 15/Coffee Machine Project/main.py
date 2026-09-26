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
    "money": 0.0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(cost):
    received = 0.0
    attempts = 0
    while received < cost and attempts < 10:
        type_of_coin = input("Insert coin (quarters, dimes, nickels, pennies): ").lower()
        num_of_coins = int(input(f"How many {type_of_coin}? "))
        if type_of_coin == "quarters":
            received += num_of_coins * 0.25
        elif type_of_coin == "dimes":
            received += num_of_coins * 0.10
        elif type_of_coin == "nickels":
            received += num_of_coins * 0.05
        elif type_of_coin == "pennies":
            received += num_of_coins * 0.01
        print(f"Total received: ${received:.2f}")
        print(f"Remaining amount: ${cost - received:.2f}")
        attempts += 1

    if attempts >= 10 and received < cost:
        return False
    if received > cost:
        change = round(received - cost, 2)
        print(f"Here is ${change} in change.")
    return True

choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


while choice != "off":
    if choice == "report":
        print_report()
    elif choice in MENU:
        #check if sufficient resources are available

        if check_resources(MENU[choice]["ingredients"]):
            
            print(f"Cost is ${MENU[choice]['cost']:.2f}. Please insert coins.")
            payment_success = process_payment(MENU[choice]["cost"])
            if payment_success:
                resources["money"] += MENU[choice]["cost"]
                for item in MENU[choice]["ingredients"]:
                    resources[item] -= MENU[choice]["ingredients"][item]
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Transaction failed. Not enough money inserted.")
        else:
            print(f"Insufficent resources to make {choice}.")
    elif choice == "off":
        print("Turning off the coffee machine.")
        break
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

