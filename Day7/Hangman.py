import random

word_list = ["shark", "monkey", "hawk"]

life = 6
# Choosing random word as answer
index = random.randint(0, len(word_list) - 1)
answer = word_list[index]

stages = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]


def draw_hangman(stage):
    match stage:
        case 6:
            print(stages[0])
        case 5:
            print(stages[1])
        case 4:
            print(stages[2])
        case 3:
            print(stages[3])
        case 2:
            print(stages[4])
        case 1:
            print(stages[5])
        case 0:
            print(stages[6])


# Generating visualisation of answer lenght with underscore
def generate_spaces(lenght: int) -> list:
    generated_space = []
    for n in range(lenght):
        generated_space.append('_')
    return generated_space


def new_round(guessed_letters: list) -> list:
    i = 0
    initial_list = guessed_letters.copy()
    for n in answer:
        if n == guess_letter:
            guessed_letters[i] = guess_letter
        elif n == guessed_letters[i]:
            guessed_letters[i] = guessed_letters[i]
        else:
            guessed_letters[i] = "_"
        i += 1

    print(initial_list)
    print(guessed_letters)
    if initial_list == guessed_letters:
        global life
        life += -1
    return guessed_letters


print("Game started")
foo = ""
blanks = foo.join(generate_spaces(len(answer)))
print(blanks)

all_letter_found = False
list_of_guessed_letters = generate_spaces(len(answer))

while not all_letter_found:
    print("Input letter")
    guess_letter = input().lower()
    visible_characters = foo.join(new_round(list_of_guessed_letters))
    print(visible_characters)
    draw_hangman(life)
    if answer == visible_characters:
        all_letter_found = True
