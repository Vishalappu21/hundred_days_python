# Funtion
user = "My name is Vishal"
def my_name():
    return user.title()

print(my_name())

def to_title_case(s,t):
    return s.title() +" "+t.title()
print(to_title_case("vishal","prasanna"))

def format_name(f_name,l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return (f"my name is {first_name} {last_name}")
print(format_name("vishal","prasanna"))

# Leap Year
def is_leap_year(year):
    """this is leap year concept"""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(2025))


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)

def my_function(a):
    if a < 40:
        return "terrible"
    elif a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))
# Calculator_Program:....
import os

print("Welcome to the Calculator_Program...")

def add(n1,n2):
    return n1+n2
def subract(n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation = {
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide
}

# x = operation["*"](4,5)
# print(x)
num = float(input("Enter the Number: "))
while True:
    n1 = num
    # n1 = int(input("Enter the First Number: "))
    for values in operation:
        print(values)
    user_need = input("Enter the Mathematical Operator: ")
    n2 = int(input("Enter the Second Number: "))
    answer_1 = operation[user_need](n1,n2)
    print(f"{n1}{user_need}{n2} = {answer_1}")
    user_another_need = input(f"type 'yes' to start_again with {answer_1} or 'no' for close: ").lower()
    if user_another_need == "yes":
        num = answer_1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')