from turtle import Screen
from paddle import Paddle
from ball import Ball
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))

ball = Ball()

ball()

screen.tracer(1)
screen.listen()
screen.onkey(fun=l_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="Down")
screen.onkey(fun=r_paddle.up, key="w")
screen.onkey(fun=r_paddle.down, key="s")


screen.exitonclick()
