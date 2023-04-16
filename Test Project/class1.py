from turtle import Turtle


class TurtleTemp(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.sety(-230)
    def up(self):
        self.setheading(90)
        self.forward(20)

    def left_(self):
        self.setheading(180)
        self.forward(20)

    def right_(self):
        self.setheading(0)
        self.forward(20)
