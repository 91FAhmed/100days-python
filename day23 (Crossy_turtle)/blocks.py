from turtle import Turtle
import random


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setpos(290, 0)

    def move(self):
        new_x = self.xcor() - 10
        self.setpos(new_x, 0)

    def random_move(self):
        rnad_int = random.randint(-200, 200)
        self.setpos(0, rnad_int)
        self.move()
