from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bid_data = {}
highest_bid = 0
highest_bidder = ""
make_bid = True

while make_bid:
    bidder_name = input("what is your name?:")
    bidder_price = input("what is your bid amount?: $")

    new_bidder_data = {"name": bidder_name, "price": bidder_price}
    bid_data[bidder_name] = new_bidder_data

    bid_decision = input(
        "Type yes to continue bid or press any key to end bid \n").lower()

    if bid_decision == "yes":
        make_bid = True
        clear()
    else:
        make_bid = False

for bids in bid_data:
    current_bid = int(bid_data[bids]["price"])
    current_bidder = bid_data[bids]["name"]

    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = current_bidder

clear()

print(f"bid winner is {highest_bidder} with amount of {highest_bid}")

print("Bid summary")
for bid in bid_data:
  bidder = bid_data[bid]["name"]
  price = bid_data[bid]["price"]
  print(f" {bidder}: ${price}")

