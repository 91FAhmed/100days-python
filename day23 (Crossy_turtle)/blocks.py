from turtle import Turtle
import random


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.blocks_list = []
        self.speed_block = 5

    def create_block(self):
        rnd = random.randint(1, 6)
        if rnd == 1:
            rnad_int = random.randint(-250, 250)
            turtle_nw = Blocks()

            turtle_nw.shape("square")
            turtle_nw.shapesize(stretch_wid=1, stretch_len=2)
            turtle_nw.rnd_color()
            turtle_nw.penup()
            turtle_nw.goto(300, rnad_int)
            self.blocks_list.append(turtle_nw)

    def move(self):
        for block in self.blocks_list:
            block.backward(self.speed_block)

    def increase_speed(self):
        self.speed_block += 1

    def rnd_color(self):
        rand_r = random.randint(0, 255) / 255.0
        rand_g = random.randint(0, 255) / 255.0
        rand_b = random.randint(0, 255) / 255.0
        self.color(rand_r, rand_g, rand_b)
