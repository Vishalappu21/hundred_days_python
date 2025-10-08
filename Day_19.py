from turtle import Turtle,Screen
import random
#
x = Turtle()
y = Screen()
def move_forward():
    x.forward(10)
def move_backward():
    x.backward(10)
def turn_left():
    new = x.heading()+10
    x.setheading(new)
def turn_right():
    new_1 = x.heading()-10
    x.setheading(new_1)
def clear_screen():
    x.clear()

y.listen()
y.onkey(move_forward,"w")
y.onkey(move_backward,"s")
y.onkey(turn_left,"a")
y.onkey(turn_right,"d")
y.onkey(clear_screen,"c")
y.exitonclick()


screen = Screen()
screen.setup(width= 500,height=600)
user = screen.textinput(title="Make You Bet",prompt="Which Turtle will Win the Race?Enter the Colour: ").lower()
colour = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtle = []

for i in range(0,6):
        tim_vishal= Turtle(shape="turtle")
        tim_vishal.penup()
        tim_vishal.color(colour[i])
        tim_vishal.goto(x = -230, y = y_positions[i])
        all_turtle.append(tim_vishal)
if user:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            win = turtle.pencolor()
            if win == user:
                print("You Won")
            else:
                print(f"{win}")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()


# 