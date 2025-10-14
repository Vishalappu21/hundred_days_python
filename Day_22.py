from turtle import Turtle,Screen
from data import paddle,ball,scorecard
import time

window = Screen()
window.setup(width=800,height=600)
window.bgcolor("black")
window.title("Pong")
window.tracer(0)
r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))
ring = ball()
score_point = scorecard()
window.listen()

window.onkey(r_paddle.up,"Up")
window.onkey(r_paddle.down,"Down")
window.onkey(l_paddle.up,"d")
window.onkey(l_paddle.down,"f")

game_on = True
while game_on:
    time.sleep(-1)
    window.update()
    ring.move()

    if ring.ycor() > 280 or ring.y_move < -280:
        ring.bounce_y()

    if ring.distance(r_paddle) < 50 and ring.xcor() > 320 or ring.distance(l_paddle) < 50 and ring.xcor() > -320:
        ring.bounce_x()

    if ring.xcor() > 380:
        ring.reset_1()
        score_point.l_point()

    if ring.xcor() < -380:
        ring.reset_1()
        score_point.r_point()


window.exitonclick()
