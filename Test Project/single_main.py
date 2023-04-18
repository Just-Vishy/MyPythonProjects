from turtle import Turtle, Screen
import random
COLORS = ["blue", "red", "green", "orange", "purple", "brown", "pink"]

shape = Turtle()
screen = Screen()
new_color = random.choice(COLORS)
def random_walk():
    shape.hideturtle()
    shape.dot(size=5, )
screen.exitonclick()
