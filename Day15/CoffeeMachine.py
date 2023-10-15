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
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

def resources_raport():
    print(
        f"Water:{resources['water']}ml\n"
        f"Milk:{resources['milk']}ml\n"
        f"Coffee:{resources['coffee']}g\n"
        f"Money:{resources['money']}$\n"
    )

    
coffee_machine_active = True

while coffee_machine_active:
    break
print("What would you like?")
print("Espresso, Latte, Cappuccino")
choice = input().lower()


match choice:
    case "espresso":
        print("Espresso case")
    case "latte":
        print("Latte case")
    case "cappuccino":
        print("Cappuccino case")
    case "off":
        print("Off case")
    case _:
        print("default case")


resources_raport()


purchase_successful = True
enough_resources = True