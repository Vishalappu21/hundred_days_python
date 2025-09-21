# Black_Jacket_Program...
from numpy.f2py.symbolic import eliminate_quotes

print("Welcome to the Balck_Jacket_Program..")
import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has Blackjack "
    elif u_score == 0:
        return "Win with a Blackjack "
    elif u_score > 21:
        return "You went over. You lose "
    elif c_score > 21:
        return "Opponent went over. You win "
    elif u_score > c_score:
        return "You win "
    else:
        return "You lose "


user_card = []
computer_card = []
computer_score = -1
user_score = -1
game_over = False
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
while not game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"Your Cards :{user_card} and current_score: {user_score}")
    print(f"computer first card: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        user_another_need = input("Type 'y' to get another card or 'n' to pass: ")
        if user_another_need == "y":
            user_card.append(deal_card())
        else:
            game_over = True
while computer_score != 0 and computer_score <17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)

print(compare(user_score,computer_score))