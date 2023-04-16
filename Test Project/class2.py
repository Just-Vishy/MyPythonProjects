import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
segment = []
color = ["red", "green", "orange", "purple", "pink", "yellow", "blue", "brown"]

class Cars:

    def __init__(self):
        super().__init__()
        self.tim = None
        self.x_position = [190, 210, 230]
        self.y_position = [230, 170, 110, 50, -10, -70, -130]

    def combined(self):
        for position_x in self.x_position:
            random_color = random.choice(color)

            for position_y in self.y_position:
                new_segment = Turtle("square")
                new_segment.penup()
                new_segment.goto(x=position_x, y=position_y)
                new_segment.color(random_color)

                segment.append(new_segment)



