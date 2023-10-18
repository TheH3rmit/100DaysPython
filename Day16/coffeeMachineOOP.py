from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine

menu = Menu()
coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()


def handle_input() -> str:
    print("What would you like?")
    print(menu.get_items())
    return input().lower()


while True:
    user_input = handle_input()
    selected_drink = MenuItem
    if user_input == "report":
        coffeeMachine.report()
        moneyMachine.report()

    for item in menu.menu:
        if user_input == item.name:
            selected_drink = item
            break
    else:
        print("Item not found in the menu.")
        continue

    if coffeeMachine.is_resource_sufficient(selected_drink):
        if moneyMachine.make_payment(selected_drink.cost):
            coffeeMachine.make_coffee(selected_drink)
        else:
            continue
    else:
        print("Not enough resources")
        continue
