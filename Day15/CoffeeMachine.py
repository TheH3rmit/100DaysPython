import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_report():
    print(
        f"Water:{resources['water']}ml\n"
        f"Milk:{resources['milk']}ml\n"
        f"Coffee:{resources['coffee']}g\n"
        f"Money:{profit}$\n"
    )


def handle_input() -> str:
    print("What would you like?")
    print("Espresso, Latte, Cappuccino")
    return input().lower()


def handle_choice(chosen: str):
    match chosen:
        case "espresso":
            print("Espresso case")
            return chosen
        case "latte":
            print("Latte case")
            return chosen
        case "cappuccino":
            print("Cappuccino case")
            return chosen
        case "report":
            print("report case")
            resources_report()
        case "off":
            print("Off case")
            for n in range(5):
                print(f"Machine shutting down in {5-n} seconds")
                time.sleep(1)
            exit(0)
        case _:
            print("default case")


def resources_check(chosen_product: str, resources_list: dict, menu: dict) -> bool:
    for i in menu[chosen_product]["ingredients"]:
        difference = resources_list[i] - menu[chosen_product]["ingredients"][i]
        if difference < 0:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True


def make_coffee(chosen_product: str, resources_list: dict, menu: dict) -> str:
    for i in menu[chosen_product]["ingredients"]:
        resources_list[i] -= menu[chosen_product]["ingredients"][i]
    return f"Here is your {chosen_product}. Enjoy!"


def handle_coins() -> float:
    print("Insert coins")
    credit = float(input())
    return credit


def purchase_check(inserted_coins, chosen_product: str, menu: dict) -> bool:
    global profit
    if inserted_coins >= menu[chosen_product]["cost"]:
        difference = inserted_coins - menu[chosen_product]["cost"]
        profit += menu[chosen_product]["cost"]
        if difference > 0:
            print(f"Returning {difference}")
        return True
    else:
        print(f"Sorry that's not enough money. {inserted_coins} refunded.")
        return False


profit = 0
coffee_machine_active = True
order_in_progress = False
while coffee_machine_active:
    if not order_in_progress:
        choice = handle_input()
        handle_coins(choice)
        enough_resources = resources_check(handle_choice(choice), resources, MENU)
        successful_purchase = purchase_check(handle_coins(), handle_choice(choice), MENU)
        if enough_resources and successful_purchase:
            make_coffee(choice, resources, MENU)
            order_in_progress = False
