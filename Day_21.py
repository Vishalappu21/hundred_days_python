# Inheritance
# -> Parent Class...

class name:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        return f"my name is {self.fname} {self.lname}"
# my_name = name("Vishal","Prasanna")
# print(my_name.display())

# -> Child_Class!..
class student(name):
    def __init__(self,fname,lname):
        name.__init__(self,fname,lname)

# name = student("Appu","Purushothaman")
# print(name.display())

# -> Adding """SUPER"""

class anbu(name):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x = anbu("STEP","THE_HINDU")
print(x.display())

# QUIZZ!..
class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        return ("Woof, woof!")

class lab(Dog):
    def __init__(self):
        self.temperament = "friendly"
lab_1 = lab()
print(lab_1.temperament)
print(lab_1.bark())


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"



doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")


sparky = Labrador()
sparky.bark()