import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']

number_of_letters = int(input("How many letters in password\n"))
numbers_of_numbers = int(input("How many numbers in password\n"))
number_of_symbols = int(input("How many symbols in password\n"))

characters_total = number_of_letters + number_of_symbols + numbers_of_numbers
password = ""

for n in range(0, characters_total):
    roll = random.randint(0, 2)
    match roll:
        case 0:
            password += letters[random.randint(0, len(letters)-1)]
        case 1:
            password += numbers[random.randint(0, len(numbers)-1)]
        case 2:
            password += symbols[random.randint(0, len(symbols)-1)]

print(password)
