# TODO-1: Ask the user for input
print("Enter name and bid information")
name = input("Enter bidder name")
bid = input("Enter bid amount (as integers)")
user_bid = {}
user_bid[name] = bid ## TODO-2: Save data into dictionary {name: price}
more_bidders = "Yes"

while more_bidders == "Yes":
    print("\n"*10)
    name = input("Enter bidder name")
    bid = input("Enter bid amount (as integers)")
    user_bid[name] = bid
    more_bidders = input("Are there other bids?")

print(user_bid)

max_bid = -1
max_bidder = None
for bidder in user_bid:
    if int(user_bid[bidder]) > max_bid:
        max_bid = int(user_bid[bidder])
        max_bidder = bidder
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(f"The maximum bid is from {max_bidder} for the amount {max_bid}.")
