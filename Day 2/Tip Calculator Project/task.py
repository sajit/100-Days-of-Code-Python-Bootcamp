print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount = bill * tip * .01
per_person_amount  = (bill + tip_amount)/people
print(f"{per_person_amount:.2f}")

