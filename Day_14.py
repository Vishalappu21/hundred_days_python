# Higher_Lower_Game:...
import random
from Learn import data
#Number_1

number = random.randint(0,100)
computer_guess = number

while True:
    try:
        my_choice = int(input("Enter the Number: "))
        if my_choice > computer_guess:
            print(f"Too High...{my_choice} is greater than {computer_guess}")
        elif my_choice < computer_guess:
            print(f"Too Low....{my_choice} is Lower than {computer_guess}")
        else:
            print(f"I found it...{my_choice} is Equal to  {computer_guess}")
            break
    except ValueError:
            print("Invalid Input enter the integer")

# Number_2:..
def computer_id():
    x = random.choice(data)
    return x['follower_count']
def user_id():
    y = random.choice(data)
    return y['follower_count']
while True:
    try:
        user = user_id()
        computer = computer_id()
        if user > computer:
            print(f"Too High..{user} and {computer}")
        elif user < computer:
            print(f"Too Low...{user} and {computer}")
        else:
            print(f"Both are Equal...{user} and {computer}")
            break
    except ValueError:
        print("Ivalid Input")
        
# Number_3:...
def get_data(acc):
    acc_name = acc['name']
    acc_fc = acc['follower_count']
    acc_desc = acc['description']
    acc_country = acc['country']
    return f"{acc_name},a {acc_fc},{acc_desc} from {acc_country}"
def check_answer(user_guess,a_compare,b_compare):
    if a_compare>b_compare:
        return user_guess == "a"
    else:
        return user_guess == "b"
score = 0
game = True
while game:
    acc_a = random.choice(data)
    acc_b = random.choice(data)
    print(acc_a)
    if acc_a == acc_b:
        acc_b = random.choice(data)
    print(f"{get_data(acc_a)}")
    print(f"{get_data(acc_b)}")
    guess = input("who has More Followers?Tyes A or B: \n").lower()

    a_follower_count = acc_a['follower_count']
    b_follower_count = acc_b['follower_count']
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score += 1
        print(f"your right!..current score: {score}")
    else:
        print(f"your Wrong!...final score: {score}")
        game = False


