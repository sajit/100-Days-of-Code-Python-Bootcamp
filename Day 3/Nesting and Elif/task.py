print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))

    if age > 18:
        ticket_price = 12
    else:
        ticket_price = 7
    print(f"Ticket price {ticket_price}")
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")
