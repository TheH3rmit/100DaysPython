import math
import random

print("How many numbers in random list?")
number_of_elements = int(input())
list_of_numbers = []

# random list_of_numbers generation
for n in range(number_of_elements):
    list_of_numbers.append(random.randint(0, 100))
list_of_numbers.sort()

print("What number to look for?")
target_number = int(input())
target_found = False
index = 0
value_of_middle = 0

while True:
    list_of_numbers_lenght = len(list_of_numbers)
    if list_of_numbers_lenght == 0:
        print("Target number not found")
        break

    index = list_of_numbers_lenght // 2  # getting the middle value_of_middle element of list_of_numbers
    value_of_middle = list_of_numbers[index]
    if target_number > value_of_middle:
        del list_of_numbers[index]  # includes deletion of value under currently selected index
        del list_of_numbers[:index]  # deletes all elements before index
    elif target_number < value_of_middle:
        del list_of_numbers[index:-1]  # deletes all elements after index
    elif value_of_middle == target_number:
        print(f"Target number found at index {index} of the list")
        break
