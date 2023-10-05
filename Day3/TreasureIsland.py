print("This is an 'iteractive' adventure")

# first_choice
print("You are in a dungeon and you must get out")
print("Choose your way forward")
print("Which door you want to open red or blue one?")
print("Available choices: red, blue")
first_choice = input().lower()
print("You have chosen: " + first_choice)
if first_choice == "red":
    print("You have died to a trap")
    exit()
else:
    print("You proceed further")

# second_choice
print("You see a lever and a hallway")
print("Do you want to pull it or leave it as it is and just go though the hallway")
print("Available choices: pull, leave")
second_choice = input().lower()
print("You have chosen: " + second_choice)
if second_choice == "pull":
    print("You have died to a trap")
    exit()
else:
    print("You proceed further")

# third_choice
print("You see the light at the end of the hallway")
print("There is a problem you see the hallway splits into three ways")
print("Available paths: left, middle, right")
third_choice = input().lower()
print("You have chosen: " + third_choice)
if third_choice == "left" or third_choice == "right":
    print("You have died to a trap")
    exit()
else:
    print("You have escaped")