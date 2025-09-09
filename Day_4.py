import random
x = random.randint( 2 , 8)
print(x)
y = random.uniform(1.6,1.8)
print(y)
z = random.random()*10
print(z)

# Heads or tails
c_1 = random.choice(['win', 'lose', 'draw'])
print(c_1)
c_2 = random.choice(['Heads','Tails'])
print(c_2)
c_3 = random.randint(0,1)
if c_3 == 0:
    print("Heads")
else:
    print("Tails")
nums_1 = [5, 10, 15, 20, 25, 30, 35, 40]
print(nums_1[2:6])
print(nums_1[-7:-3])
print(nums_1[:6])
print(nums_1[::2])
nums_2 = ["Vishal","Prasanna"]
var = [nums_2,nums_1]
print(var[1][3])

# Bill_payment Random
friends = ['Vishal','vimal','santhosh','gauri','sashikanth']
bill_payment  = random.choice(friends)
print(f"The person who needs to pay the bill is {bill_payment}")

text = 'Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand,West Bengal'
new_txt= [i.strip() for i in text.split(",")]
print(len(new_txt))
print(new_txt[0])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
# print(fruits)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

# rock paper scissor Project...
print("Welcome to Rock_Paper_Scissor Game..")
choice_1 = ['rock','paper','scissor']
computer_c_1 = random.choice(choice_1)
user_choice = input('rock,paper,scissor: ').lower()
print(f"User_choice:{user_choice} ")
if user_choice == computer_c_1:
    print("The Game is Tie...")
elif user_choice == 'rock' and computer_c_1 == 'scissor':
    print("User Win the Game...")
elif user_choice == 'scissor' and computer_c_1 == 'paper':
    print("User Win the Game...")
elif user_choice == 'paper' and computer_c_1 == 'rock':
    print("User Win the Game...")
else:
    print("Computer win the Game..")

print("hello")
