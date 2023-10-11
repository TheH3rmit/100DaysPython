import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # deck of 52
print(len(deck))


def fill_shuffle_deck() -> list:
    global deck
    new_deck = deck.copy()
    new_deck = random.sample(new_deck, len(deck))
    return new_deck


def hand_distribution():
    player_hand.append(playing_deck.pop())
    player_hand.append(playing_deck.pop())
    dealer_hand.append(playing_deck.pop())


def hit():
    dealer_hand.append(playing_deck.pop())


def stand():
    return


player_hand = []
dealer_hand = []

game_finished = False


def evaluate_cards():
    if sum(player_hand) > 21 or sum(dealer_hand) == 21:
        print("Dealer wins")
        return False
    elif sum(player_hand) == 21:
        print("Player won")
        return False
    elif sum(player_hand) > sum(dealer_hand) and sum(dealer_hand) < 21:
        print("Player won")
        return False
    elif sum(dealer_hand) > 21:
        print("Player won")
        return False
    else:

        return True


while not game_finished:
    playing_deck = fill_shuffle_deck()
    hand_distribution()
    state = True
    while state:
        print(f"Dealer cards:{dealer_hand}")
        print(f"Player cards:{player_hand}")
        print("Hit or Stand")
        response = input().lower()
        if response == "hit":
            hit()
        elif response == "stand":
            stand()
            if sum(player_hand) > sum(dealer_hand):
                dealer_hand.append(playing_deck.pop())
        else:
            print("I don't understand")
        print(f"Dealer cards:{dealer_hand}")
        print(f"Player cards:{player_hand}")
        state = evaluate_cards()
