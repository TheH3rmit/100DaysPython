import random

word_list = ["shark", "monkey", "hawk"]

# Choosing random word as answer
index = random.randint(0, len(word_list) - 1)
answer = word_list[index]


# Generating visualisation of answer lenght with underscore
def generate_spaces(lenght: int) -> str:
    i = 0
    generated_space = ''
    while i < lenght:
        generated_space += '_'
        i += 1
    return generated_space


def new_round() -> str:
    guessed_letters = ""
    for n in range(len(answer)):
        if answer[n] == guess_letter:
            # print("Yes letter chosen is in the word")
            guessed_letters += guess_letter
        else:
            # print("No letter chosen is not in the word")
            guessed_letters += '_'
    return guessed_letters


print("Game started")
blanks = generate_spaces(len(answer))
print(blanks)

all_letter_found = False
while not all_letter_found:
    print("Input letter")
    guess_letter = input().lower()
    visible_characters = new_round() # TODO fixing coping guessed letters to prevent loss of previously guessed letters
    print(visible_characters)
    if answer == visible_characters:
        all_letter_found = True
