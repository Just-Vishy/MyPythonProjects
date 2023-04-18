COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []


class CarManager:

    def __init__(self):
        from turtle import Turtle
        self.car_body = Turtle("square")
        self.car_body.setheading(180)
        self.car_body.penup()


    def car(self):
        self.car_body.forward(STARTING_MOVE_DISTANCE



