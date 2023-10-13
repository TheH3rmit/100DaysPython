import random


def fill_shuffle_deck() -> list:
    global deck
    new_deck = deck.copy()
    new_deck = random.sample(new_deck, len(deck))
    return new_deck


def hit(hand: list):
    hand.append(playing_deck.pop())


def hand_distribution():
    hit(player_hand)
    hit(player_hand)
    hit(dealer_hand)


def blackjack_check() -> bool:
    if sum(player_hand) == 21 or sum(dealer_hand) == 21:
        return True
    else:
        return False


def bust_check() -> bool:
    if sum(player_hand) > 21 or sum(dealer_hand) > 21:
        return True
    else:
        return False


def evaluate_game():
    if sum(dealer_hand) == sum(player_hand):
        print("Draw")
    elif sum(player_hand) < sum(dealer_hand) <= 21 or sum(player_hand) >= 21:
        print("Lose")
    elif sum(dealer_hand) < sum(player_hand) <= 21 or sum(dealer_hand) >= 21:
        print("Win")


def new_round_setup():
    global playing_deck
    player_hand.clear()
    dealer_hand.clear()
    playing_deck = fill_shuffle_deck()
    hand_distribution()


def blackjack():
    new_round_setup()
    game_active = True
    show_hands()
    while game_active:
        if blackjack_check() or bust_check():
            break
        game_active = handle_input()
    evaluate_game()


def show_hands():
    print(f"Dealer cards:{dealer_hand}")
    print(f"Player cards:{player_hand}")


def bot_decision():
    while True:
        if sum(player_hand) > sum(dealer_hand):
            hit(dealer_hand)
        else:
            show_hands()
            break
    return False


def handle_input():
    correct_input = False
    while not correct_input:
        print("Hit or Stand")
        response = input().lower()
        if response == "hit":
            hit(player_hand)
            show_hands()
            if blackjack_check() or bust_check():
                return False
        elif response == "stand":
            return bot_decision()
        else:
            print("I don't understand")


player_hand = []
dealer_hand = []

game_finished = False
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # deck of 52
playing_deck = []

next_game = True
while next_game:
    print("Do you want to play blackjack YES/NO")
    decision = input().lower()
    if decision == "yes":
        blackjack()
    elif decision == "no":
        exit()
    else:
        "I don't understand"