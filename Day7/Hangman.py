import random


# Stages for hangman to display
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


# Generating visualisation of answer lenght with underscore and returns it
def generate_underscore_list(lenght: int) -> list:
    generated_space = []
    for n in range(lenght):
        generated_space.append('_')
    return generated_space


#Checks provided list if guess_letter is in the answer and deduces lives for wrong guess
def guess_letter_round(guessed_letters: list) -> list:
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
    if initial_list == guessed_letters:
        global life
        life += -1
    return guessed_letters



#handles the when the game ends
def game_end_condition():
    global game_running
    if answer == visible_characters and life > 0:  # check if all letters are the same to trigger win and end program
        game_running = False
        print("You win")
    else:
        game_running = False
        print("You lose out of lives")


word_list = ["shark", "monkey", "hawk"]

life = 6
# Choosing random word as answer
index = random.randint(0, len(word_list) - 1)
answer = word_list[index]

print("Game started")
output = ""
blanks = output.join(generate_underscore_list(len(answer))) # converts list of characters in a string
print(blanks)

game_running = True
list_of_guessed_letters = generate_underscore_list(len(answer))


while game_running:
    print("Input letter")
    guess_letter = input().lower()
    visible_characters = output.join(guess_letter_round(list_of_guessed_letters)) # converts list of characters in a string
    print(visible_characters)
    draw_hangman(life)

    game_end_condition()
