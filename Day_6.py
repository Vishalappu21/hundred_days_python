# def my_fun():
#   print("Hello")
# print("Bye")
# def my_function():
#     a = 3
#     if a > 2:
#         print("This Will run")
# my_function()
#
# # While_Loops..
# n = 0
# while n<10:
#     n+=1
#     print(n)
# n = 0
# user = int(input("enter 0 to stop: "))
# while user != 0:
#     n += user
#     user = int(input("enter 0 to stop: "))
# print(n)
# import random
# com_choice = random.randint(1,50)
# user_int = int(input("Enter the Number: "))
# while user_int != com_choice:
#     user_int = int(input("Enter the Number: "))

# n = 1
# m = 5
# while n<11:
#     result = n*m
#     print(result)
#     n += 1
#
# user_int = int(input("Enter the Number: "))
# while user_int >= 0:
#     print(user_int)
#     user_int -=1
#
# user_value = int(input("Enter the Number: "))
# while user_value<10:
#     user_value += 1
#     print("Vishal is the Good Boy")

num = int(input("Enter the Digitis: "))
reverse = 0
while num > 0:
    x = num % 10
    reverse = reverse * 10 + x
    num = num // 10

print(f"Reverse number {reverse}")

n = 0
while n<5:
    n = n+1
    print("hello")