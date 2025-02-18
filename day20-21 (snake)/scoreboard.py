from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=275)

    def sc_board(self):
        self.write(
            f"Score:{self.score}", align="center", font=("Space Mono", 12, "normal")
        )

    def update_score(self):
        self.score += 1
        self.clear()
        self.sc_board()


class GameOver(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.draw_gameover()
        self.write(f"Game Over", align="center", font=("Space Mono", 12, "normal"))

    def draw_gameover(self):
        self.draw_scoreboard()
        self.goto(0, 0)
