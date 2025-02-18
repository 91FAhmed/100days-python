from turtle import Turtle


class paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.x_axis = 350
        self.where = pos

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setpos(self.where)

    def go_up(self):
        self.goto(y=self.ycor() + 20, x=self.where[0])

    def go_down(self):
        self.goto(y=self.ycor() - 20, x=self.where[0])
