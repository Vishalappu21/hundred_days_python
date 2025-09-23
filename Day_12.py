Scopes
my_enemies = 1
def enemies():
    my_enemies = 2
    print(f"my enemies are {my_enemies}")

enemies()
print(f"my enemies are {my_enemies}")

# Local_Scope:..
def STEP_The_hindu():
    head_of_operations = "Rujith"
    print(f"the Head of operations is {head_of_operations}")
STEP_The_hindu()

# Global_Scope:....
marks = 10
                  # -> Name Space

def internal():
    marks = 5
    print(f"he got {marks} in maths")
internal()
print(f"he got {marks} in science")

# Prime_Number:...
num = 4
def is_prime_num():
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
print(is_prime_num())

# modify the Global_Scope
marks = 10
                  # -> Name Space

def internal():
    global marks
    marks = 5
print(f"he got {marks} in maths")
internal()
print(f"he got {marks} in science")

# Declare a global variable
global_variable = 10

def modify_global():
    # Use the 'global' keyword to indicate that we are modifying the global_variable
    global global_variable
    global_variable = 20  # This will change the value of the global variable

print(f"Before modification: {global_variable}")
# modify_global()
print(f"After modification: {global_variable}")

# Number Guessing Program:...
import random
from random import randint

print("welcome to Number_Guessing_Game:.....")
user_guess = random.randrange(100)
computer_guess = random.randrange(100)
print(user_guess)
print(computer_guess)

def winner():
    if user_guess > computer_guess:
        print("Too High")
    elif user_guess == computer_guess:
        print("You find it")
    else:
        print("Too Low")
print(winner())

while True:
    winner()
    break


easy_level_turns = 10
hard_level_turns = 5
def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("Too High...")
        return turns -1
    elif user_guess<actual_answer:
        print("Too Low")
        return turns -1
    else:
        print(f"you got the answer {actual_answer}")
def level_difficult():
    level = input("choose the level..type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return easy_level_turns

    else:
        return hard_level_turns
def game():
    print("welcome to Number_Guessing_Game:.....")
    ans = randint(1,100)
    # print(f"your answer is: {ans}")

    turns = level_difficult()
    print(f"how many {turns} attempts you have remaining")

    guess = 0
    while guess != ans:
        guess = int(input("Enter The Number: "))
        turns = check_answer(user_guess=guess,actual_answer=ans,turns=turns)
        if turns == 0:
            print("You don't have More attempts")
            break

game()


