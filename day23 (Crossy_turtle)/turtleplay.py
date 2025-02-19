from turtle import Turtle


class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.setposition(0, -280)

    def move_up(self):
        self.forward(10)
