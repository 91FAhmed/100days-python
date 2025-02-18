from turtle import Turtle

position = [(0.0, 0.0), (-10.0, 0.0), (-20.0, 0.0)]


class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        for pos in position:
            self.add_parts(pos)

    def move(self):
        for seg_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[seg_num - 1].xcor()
            new_y = self.body_parts[seg_num - 1].ycor()
            self.body_parts[seg_num].goto(new_x, new_y)
        self.body_parts[0].forward(10)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def add_parts(self, lenx):
        body = Turtle()
        body.color("green")
        body.penup()
        body.shape("square")
        body.goto(lenx)
        self.body_parts.append(body)

    def extend(self):
        self.add_parts(self.body_parts[-1].pos())
