import random

game_state = True
player_choice = 0


def choice_handle(temp: int, user: str):
    match temp:
        case 0:
            print(f"{user} have chosen rock")
        case 1:
            print(f"{user} have chosen paper")
        case 2:
            print(f"{user} have chosen scissors")
        case _:
            print("No suitable case")


def winner_handle(player: int, cpu: int):
    if player == cpu:
        print("Draw")
    elif player == 0 and cpu == 1:
        print("CPU Wins")
    elif player == 1 and cpu == 2:
        print("CPU Wins")
    elif player == 2 and cpu == 0:
        print("CPU Wins")
    elif player == 0 and cpu == 2:
        print("Player Wins")
    elif player == 1 and cpu == 0:
        print("Player Wins")
    elif player == 2 and cpu == 1:
        print("Player Wins")


while game_state:
    print("Type 0 for Rock, 1 for Paper, 2 for Scissors")
    player_choice = int(input())
    choice_handle(player_choice,"Player")
    cpu_choice = random.randint(0, 2)
    choice_handle(cpu_choice, "CPU")
    winner_handle(player_choice, cpu_choice)
    print("To close game input: exit")
    print("To continue press enter")
    if input().lower() == "exit":
        game_state = False
        exit()