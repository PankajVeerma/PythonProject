import os


def find_Winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidder_price = bidder_details[bidder]
        if bidder_price >= highest_bid:
            highest_bid = bidder_price
            winner = bidder
            print(f"Here is the list of All Bidder is :-{bidder_details}")
    print(f"The Winner is :- {winner} with a bid pric :- {highest_bid}")


print()
print()
print()
print()

print("                                               WElCOME TO AUCTION PROGRAM")
bidder_data = {}
end_of_biddibg = False
while not end_of_biddibg:
    name = input("Enter your name:-")
    price = int(input("What is your bid ? :- "))
    bidder_data[name] = price
    more_bidder = input("Are you more bidder? type 'Yes' or 'No' :- ").lower()
    if more_bidder == "no":
        end_of_biddibg = True
        find_Winner(bidder_data)
    elif more_bidder == "yes":
        os.system("cls")
    else:
        print("Invailed Input")
        break
