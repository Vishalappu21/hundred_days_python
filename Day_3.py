# If_or_Else Condition
age = 5
if age > 18:
    print('you are allowed to watch the movie "Collie"')
else:
    print("you are not allowed to watch the movie")

print("Welcome to the Rollercoster Ride")
height = int(input("Please tell your height in cm: "))
minimum_height = 120
bill = 0
if height >= minimum_height:
    print("you can ride in the Rollercoster")
    age = int(input("Please tell your age: "))
    if age <= 12:
        bill = 5
        print("you can ride,The ticket Price is 80")
    elif age <= 18:
        bill = 10
        print("you need to pay 100 for the ticket")
    elif 45 <= age <= 55:
        print("Have a free ride")
    else:
        bill = 20
        print("you need to pay 150 for the ticket")
    photo_need  = input("Do yo want the photo of your ride.Type Y for Yes or N for No: ").lower()
    if photo_need == "y":
        bill = bill + 5
    print(f"Your Final bill is: {bill}")
else:
    print("you can't ride in the rollercoster,because your height is below than minimum height")
# Modulo operator //
ned = 10//3
print(ned)

Number = 10
if Number % 2 == 0:
    print("The Number is an Even Number")
else:
    print("The Number is a Odd Number")

# BMI Calculator
weight = 85
height = 1.85
bmi = weight/(height**2)
print(f"Your BMI is:{round(bmi)}")
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("Overweight")

# Pizza delivery Project
print("Welcome to The Python Pizza Delivery!")
size = input("what size Pizza do you Want? S for Small,M for Medium or L for Large:").lower()
pepperoni = input("do you want pepperoni on Pizza? Type Y for yes or N for No: ").lower()
extra_chesse = input("do you want extra cheese? Type Y for Yes or N for No: ").lower()

bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 30
else:
    print("You enter the wrong input,Thank You😫")
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_chesse == "y":
    bill += 1
print(f"your total bill is {bill}

# Driving Licence Test:
age = 15
driving_test = True
if age >= 18 and driving_test:
    print("Eligible")
else:
    print("Not eligible")

ticket_age = 61
if ticket_age < 12 or ticket_age > 60:
    print("Discount Available")
else:
    print("Discount Not Available")

a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
# Day_3 Project Treasure Island...
print("Welcome to Treasure Island.Your mission is to find the treasure")
user_input = input('You\'re at a Cross Road. Where do you want to go? Type "Left" or "Right": ' ).lower()
if user_input == "left":
    print("You've come to the Lake.There is an Island in the Middle of the Lake ")
    choice_2 = input('you\'ve come to lake.Do you want to "wait" for a Boat or "Swin" across: ').lower()
    if choice_2 == "wait":
        print("Good choice! You waited and got a safe boat ride .")
        choice_3 = input('you\'ve reached the Entrance safely. which door you will like to Open?.type "red" or "yellow" or "Blue": ').lower()
        if choice_3 == "red":
            print("Burned by fire.Game Over😫")
        elif choice_3 == "yellow":
            print("You Win!😎")
        elif choice_3 == "blue":
            print("Eaten by beasts.Game Over🤦‍♀️")
        else:
            print("invalid input.Game Over...!")
    elif choice_2 == "swim":
        print("Oh no,you were attacked by big crocodile!....")
    else:
        print("Invalid choice,Game Over...!")
elif user_input == "right":
    print("Fall into a hole.Game Over")
else:
    print("invaid input,Game Over...!")