number = 735_25.965
print(type(number))

print(len(str(12345600)))

intiger = 12345
print(type(intiger))
string = "Vishal_Prasanna"
print(type(string))
float = 2356.021
print(type(float))
boolean = True
print(type(boolean))

Name = input("Enter Your Name: ")
len_of_Name = len(Name)
print(Name)
print("Length of the Name :" + str(len_of_Name))

divide = 6//3
print(divide)
print(3*3+3/3-7)

#BMI Calculator
height = 1.65
weight = 84
# Write your code here.
# Calculate the bmi using weight and height.
bmi =weight/height**2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 5))

# Number Manipulation
num = 1
num +=3
print(type(num))
print(num)
# F-String
print(f"your number is {num}")

# TIP CALCULATOR
print("Welcome to the TIP CALCULATOR")
bill = int(input("What is your Total Bill? "))
print(bill)
tip = int(input("How Much tip would you like to Give? 10,12 or 15: "))
print(tip)
no_of_person = int(input("How many people to split the Bill? "))
print(no_of_person)
tip_percent = tip/100
print(tip_percent)
total_bill = bill+(bill*tip_percent)
print(total_bill)
total_bill_person = total_bill/no_of_person
print(total_bill_person)

