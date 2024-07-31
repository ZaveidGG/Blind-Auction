from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

hasBidder = True
bidderDict = {}
def clear():
    os.system('cls || clear')

def findWinner(bidderDict):
    highestBid = 0
    for bidder in bidderDict:
        bid_amount = bidderDict[bidder]
        if bid_amount > highestBid:
            highestBid = bid_amount
            winnerName = bidder
        else:
            highestBid = highestBid
            winnerName = bidder

    print(f"The winner is {winnerName} with a bid of ${highestBid}")

while hasBidder:
    name = input("What is your name?:\n")
    bid = int(input("What's your bid?: \n$"))
    bidderDict[name]=bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'\n")
    clear()

    if choice.lower() == 'no':
        hasBidder = False
        highestBid = max(bidderDict.values())
        findWinner(bidderDict)
    elif choice.lower() != 'yes':
        print("You have entered an invalid choice")
        hasBidder = False





