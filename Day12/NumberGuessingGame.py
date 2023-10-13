import random


def validate_input(new_int: str) -> int:
    global lives
    while True:
        try:
            new_int = int(new_int)
            lives -= 1
        except:
            print("Please use numeric digits")
            continue
        if 0 > new_int > 100:
            print("Number chosen is out of range")
        return new_int


def set_lives_difficulty(difficulty: str) -> int:
    match difficulty:
        case "hard":
            guesses_limit = 10
            return guesses_limit
        case "normal":
            guesses_limit = 20
            return guesses_limit
        case "easy":
            guesses_limit = 30
            return guesses_limit


def lose_condition_check(number_of_guesses) -> bool:
    if number_of_guesses == 0:
        print("You lost")
        return True
    return False


def main_game_loop():
    print(f"You have {lives} chances to guess correct number")
    print("Choose a number between 0 and 100 including")
    user_guess = input()
    user_guess = validate_input(user_guess)
    if answer == user_guess:
        print(f"You are correct the number that I had in mind was {answer}")
    elif answer > user_guess:
        print(f"The number that I'm thinking about is larger than {user_guess}")
    elif answer < user_guess:
        print(f"The number that I'm thinking about is smaller than {user_guess}")


while True:
    answer = random.randint(0, 100)
    print("Write 'Hard', 'Normal', 'Easy' to choose difficulty level of the game'")
    difficulty = input().lower()
    lives = set_lives_difficulty(difficulty)
    while not lose_condition_check(lives):
        main_game_loop()
