from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 280)
        self.score = 0
        self.write(f"Score:{self.score}", align="left", font=("Arial", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}", align="left", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.penup()
        self.hideturtle()
        self.write("Game Over", align="center", font=("Arial", 12, "normal"))
