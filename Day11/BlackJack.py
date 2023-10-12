import random


def fill_shuffle_deck() -> list:
    global deck
    new_deck = deck.copy()
    new_deck = random.sample(new_deck, len(deck))
    return new_deck


def hit(hand: list):
    hand.append(playing_deck.pop())
    evaluate_cards()


def hand_distribution():
    hit(player_hand)
    hit(player_hand)
    hit(dealer_hand)


player_hand = []
dealer_hand = []

game_finished = False


def evaluate_cards():
    if sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print("Dealer won")
        new_round_setup()
    elif sum(player_hand) == 21 or sum(dealer_hand) > 21:
        print("Player won")
        new_round_setup()
    elif sum(dealer_hand) == 21 or sum(player_hand) > 21:
        print("Dealer won")
        new_round_setup()


def evaluate_game():
    if sum(dealer_hand) > sum(player_hand):
        print("Dealer won")
    elif sum(dealer_hand) < sum(player_hand):
        print("Player won")
    new_round_setup()


def new_round_setup():
    global playing_deck
    player_hand.clear()
    dealer_hand.clear()
    playing_deck = fill_shuffle_deck()
    hand_distribution()


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # deck of 52
playing_deck = []

new_round_setup()
while not game_finished:
    print(f"Dealer cards:{dealer_hand}")
    print(f"Player cards:{player_hand}")
    print("Hit or Stand")
    response = input().lower()
    if response == "hit":
        hit(player_hand)
    elif response == "stand":
        if sum(player_hand) > sum(dealer_hand):
            hit(dealer_hand)
        else:
            evaluate_game()
    else:
        print("I don't understand")
