# How to Create Class
class vishal:
    pass
x = vishal()
print(x)

class name:
    def __init__(self,name,age):
        self.name = name
        self.age = age
y = name("vishal",45)
z = name("anbu",54)
print(y.age)
print(z.name)

class student_1:
    def __init__(self,name_std,roll_no):
        self.name_std = name_std
        self.roll_no = roll_no
    def method(self):
        return f"Name: {self.name_std}, Roll No: {self.roll_no}"
C = student_1("Vishal",101)
print(C.method())

class student_2:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def disply(self):
        return f"Name: {self.name}, Roll No: {self.roll_no},Marks: {self.marks}"
    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
c = student_2("Vishal",147,70)
d = student_2("Mukesh",999,20)
print(c.disply())
print(c.result())
print(d.disply())
print(d.result())

import statistics
class student:
    def __init__(self,name,roll_no,math,english,science):
        self.name = name
        self.roll_no = roll_no
        self.math = math
        self.english = english
        self.science = science
    def disply(self):
        return f"Name: {self.name}, Roll No: {self.roll_no},Marks: math = {self.math},english = {self.english},science= {self.science}"
    def average(self):
        avg = round(statistics.mean([self.math,self.english,self.science]))
        return avg
    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"


school = student("Vishal",147,45,50,60)
print(school.disply())
print(school.average())
print(school.grade())