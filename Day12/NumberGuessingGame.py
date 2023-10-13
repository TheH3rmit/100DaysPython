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





answer = random.randint(0, 100)


while True:
    print("Choose a number between 0 and 100 including")
    user_guess = input()
    user_guess = validate_input(user_guess)
    if answer == user_guess:
        print(f"You are correct the number that I had in mind was {answer}")
    elif answer > user_guess:
        print(f"The number that I'm thinking about is larger than {user_guess}")
    elif answer < user_guess:
        print(f"The number that I'm thinking about is smaller than {user_guess}")
