# Loops_Concept
for i in range(1,11):
    print(f"Now i is: {i}")
name = ['Vishal','prasanna','appu']
for j in name:
    print(j)

print(sum(student_score))
total_score = 0
student_score = [100,125,20,189,145,160,89,35,45,56,65,75,89,99,105,156,200,196,30,45]
for i in student_score:
    total_score += i
print(total_score)
max_score = student_score[0]
for a in student_score:
    if a > max_score:
        max_score = a
print(max_score)
# #
add_score = 0
for i in range(1,101):
    add_score += i
print(add_score)
#
for i in range(1,11,3):
    print(i)
# Fizz_Buzz Program..
for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# Day_5 password Generator Project...
import random

alpha = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
alpha_1 = [i.strip() for i in alpha.split(",")]
print(alpha_1)
num = '0,1,2,3,4,5,6,7,8,9'
numbers = [j.strip() for j in num.split(",")]
print(numbers)
sym = '@#$&*-+!?%^.:\/{}[]=()<>'
symbols = list(sym)
print(symbols)

print("Welcome to the password Generator Project..")
nr_letter = int(input("How many letters do you want in the Password?\n"))
nr_symbols = int(input("How many symbols do you want in the Password?\n"))
nr_integers = int(input("How many integers do you want in the Password?\n"))

passowrd = ""
for i in range(0,nr_letter):
    passowrd += random.choice(alpha_1)
for j in range(0,nr_symbols):
    passowrd += random.choice(symbols)
for k in range(0,nr_integers):
    passowrd += random.choice(numbers)
print(f"the final password is {passowrd}")

print("Welcome to the password Generator Project..")
nr_letter = int(input("How many letters do you want in the Password?\n"))
nr_symbols = int(input("How many symbols do you want in the Password?\n"))
nr_integers = int(input("How many integers do you want in the Password?\n"))
passowrd_list = []
for i in range(nr_letter):
    passowrd_list.append(random.choice(alpha_1))
for j in range(nr_symbols):
    passowrd_list.append(random.choice(symbols))
for k in range(nr_integers):
    passowrd_list.append(random.choice(numbers))
random.shuffle(passowrd_list)
password_1 = "".join(passowrd_list)
print(f"the final password is {password_1}")


#Random Dice Roll
dice = random.randint(1,6)
print(dice)
# Random Coin Toss
var = ["Heads","Tails"]
toss = random.choice(var)
if toss == "Heads":
    print("You won the Toss")
else:
    print("you loss the Toss")
# Random Number Guessing Game
user_number = int(input("choose any number from 1 to 50: "))
comp_choice = random.randint(1,50)
print(comp_choice)
if user_number > comp_choice:
    print("Too High...")
elif user_number == comp_choice:
    print("You find it..")
elif user_number < comp_choice:
    print("It's Too Low..")
else:
    print("Invaild Input")
# Random Lottery Number Generator
num = '0,1,2,3,4,5,6,7,8,9'
numbers = [j.strip() for j in num.split(",")]
print(numbers)
nr_integers = int(input("How many integers do you want in the Password?\n"))
lottery_number = []
for i in range(nr_integers):
    lottery_number.append(random.choice(numbers))
print(lottery_number)
lottery_number_1 = "".join(lottery_number)
print(lottery_number_1)
