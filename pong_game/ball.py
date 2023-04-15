from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = [250,-250]
        self.l_r = random.choice(self.direction)
        self.goto(self.l_r)

\
    # def move(self):
    #     self.forward(20)

    def game_over(self):
        self.write(arg="Game Over", move=False, align="center", font=("Arial", 8, "normal"))