from Learn import MENU

# list = list(MENU.items())
# print(list)
# while True:
#     def choice():
#         user_need = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if user_need == 'espresso':
#             print(list[0])
#         elif user_need == 'latte':
#             print(list[1])
#         elif user_need == "cappuccino":
#             print(list[2])
#         else:
#             print("Invaild Entry...Thank You")
#     break
# choice()
gain = 0
resources = {
    "water":300,
    "milk":200,
    "coffee":100
}

def is_resource(order_ingredients):
    is_enough = True
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print("Sorry there is not enough water.")
            return False
    return True
def process_coins():
    print("Please Insert Coins.")
    total = int(input("How Many Quarters?. "))*0.25
    total += int(input("How Many dimes?. ")) * 0.10
    total += int(input("How Many nickles?. ")) * 0.05
    total += int(input("How Many pennies?. ")) * 0.01
    return total

def transaction_successful(money_recieved,drink_cost):
    if money_recieved >=drink_cost:
        change = round(money_recieved - drink_cost,2)
        global gain
        gain += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name,order_ingrediants):
    for i in order_ingrediants:
        resources[i] -= order_ingrediants[i]
    print(f"here is your {drink_name}")
user_on = True
while user_on:
    user_need = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_need == "off":
        user_on = False
    elif user_need == "report":
        print(f"Water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${gain}")
    else:
        drink = MENU[user_need]
        if is_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment,drink['cost']):
                make_coffee(user_need,drink['ingredients'])

