from turtle import Screen
from class1 import TurtleTemp
from class2 import Cars

screen = Screen()

screen.setup(width=500, height=500)
tim = TurtleTemp()
name = tim

screen.listen()
screen.onkey(fun=name.up, key="w")
screen.onkey(fun=name.left_, key="a")
screen.onkey(fun=name.right_, key="d")
screen.onkey(fun=name.clear, key="c")
screen.tracer(0)
game_is_on = True
while game_is_on:
    cars = Cars()
    cars.combined()
    screen.update()
screen.exitonclick()
