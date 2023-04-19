import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
positions = [(0, 0), (-20, 0), (-40, 0)]
y_position = [()]
for new in range(6):
    for position in positions:
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.goto(position)

screen.exitonclick()
