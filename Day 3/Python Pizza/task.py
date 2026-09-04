print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

def get_bill_for_size(pizza_size):
    if pizza_size == "S":
        return 15
    elif pizza_size == "M":
        return 20
    else:
        return 25


bill = 0
bill += get_bill_for_size(size)
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


