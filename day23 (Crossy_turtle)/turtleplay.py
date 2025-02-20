from turtle import Turtle
from scoreboard import ScoreBoard
from blocks import Blocks


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

    def detect_win(self):
        if self.ycor() >= 295:
            ScoreBoard.update_score()
            Blocks.increase_speed()
            self.goto(0, -280)
