def decision_handle():
    print("Are there any other bidders that want to bid?")
    print("Yes/No")
    global other_bidders
    correct_input = False
    while not correct_input:
        user_decision = input().lower()
        if user_decision == "yes":
            other_bidders = True
            correct_input = True
        elif user_decision == "no":
            other_bidders = False
            correct_input = True
        else:
            print("I don't usderstand please try again")
            correct_input = False


def search_bid_winner(dictionary: dict):
    max_offer = 0
    bid_winner = ""
    for n in dictionary:
        if dictionary[n] > max_offer:
            max_offer = dictionary[n]
            bid_winner = n
    return bid_winner


other_bidders = True
bidders_bid = {}

while other_bidders:
    print("Bidder name is:")
    bidder_name = input()
    print("Enter your bid:")
    bid_cost = int(input())
    bidders_bid[bidder_name] = bid_cost
    decision_handle()

bid_winner = search_bid_winner(bidders_bid)
print(bid_winner, bidders_bid[bid_winner])
