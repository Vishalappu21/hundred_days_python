from  turtle import Screen
from Learn import Snake,food,scoreboard
import time

# snake_shape = turtle.Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game..")
screen.tracer(0)
seg = []
# def moving():
#     segment_1 = Turtle(shape="square")
#     segment_1.color("white")
#
#     segment_2 = Turtle(shape="square")
#     segment_2.color("white")
#     segment_2.goto(-20,0)
#
#     segment_3 = Turtle(shape="square")
#     segment_3.color("white")
#     segment_3.goto(-40,0)

snake = Snake()
Food = food()
score = scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    if snake.head.distance(Food)<15:
        Food.refersh()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = False
        score.game_over()

screen.exitonclick()



