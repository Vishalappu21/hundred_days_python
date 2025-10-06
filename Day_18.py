# Turtle Graphics
import turtle
x = turtle.Turtle()
x.shape("turtle")
x.color("red", "green")
def start():
    for i in range(4):
        x.forward(100)
        x.right(90)
start()
x.forward(100)
x.right(90)
x.forward(100)
x.right(90)
x.forward(100)
turtle.done()

# Importing Module and install Packages
# from - > Keyword turtle -> Module_Name import -> keyword Turtle -> thing (or) what we want from the module CLASS
# Another_One
# from turtle import *
"""Which Means you can take everything from that module"""
import turtle
# -> """Aliasing Module  as t"""
# import pandas as pd -> Alias_Name
import turtle as t
a = t.Turtle()
print(a)
#
import pendulum as pns
s = pns.now()
print(s)


x = t.Turtle()
def shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        x.forward(100)
        x.right(angle)
for _ in range(3,11):
    shape(_)

t.done()
import random
import turtle
x = turtle.Screen()
x.setup(height=600,width=600)
x.bgcolor("orange")
x.title("Random_Walk...")
y = turtle.Turtle()
y.speed(0)
y.pensize(2)
direction = [0,90,270,180]
num_step = 100
for _ in range(num_step):
    y.setheading(random.choice(direction))
    y.forward(random.randint(20,50))
x.exitonclick()