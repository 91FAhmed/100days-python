from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.update()

    def update(self):
        x_axis = random.randint(-280, 200)
        y_axis = random.randint(-280, 200)
        self.goto(x_axis, y_axis)
