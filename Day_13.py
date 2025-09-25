# Finding the Error
# Debugging:...
def my_fun():
    for i in  range(0,21):
        if i == 20:
            print("you find")
my_fun()

# Reproduce the Bug:...
import random
dice_face = ["1","2","3","4","5","6"]
choice = random.choice(dice_face)
print(choice)
x  = random.randint(0,5)
print(dice_face[x])

# read the Computer:..
# input = int(input("Enter the Year: "))
#
# if input > 1981 and input < 1996:
#     print("You are millennail")
# elif input > 1996:
#     print("You are Genz")

# while True:
#     try:
#         num = int(input("Enter the Number: "))
#         break
#     except ValueError:
#         print(f"Could not convert '{input}' to an integer.")
# if num > 18:
#     print("you are allowed to watch the Collie Movie")
# else:
#     print("you are not allowed...")

# Debugger:..
import random
def mutate(a_list):
    b_list = []
    new_item = 0
    for i in a_list:
        new_item = i * 2
        new_item += random.randint(1,3)
        new_item = sum([new_item,i])
        b_list.append(new_item)
    print(b_list)


mutate([1,2,3,4,5])

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
print(odd_or_even(5))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2024))

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
print(fizz_buzz(20))


