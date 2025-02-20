from turtle import Turtle, Screen
from turtleplay import TurtlePlayer
from blocks import Blocks
import time
from scoreboard import ScoreBoard

# Creating Screen
window = Screen()
window.setup(600, 600)
# turning animation off
window.tracer(0)
# Create turtle
turtle_plr = TurtlePlayer()
blocks = Blocks()
score = ScoreBoard()

game_is_running = True

window.listen()

window.onkey(turtle_plr.move_up, "space")

while game_is_running:
    time.sleep(0.1)
    window.update()

    blocks.create_block()
    blocks.move()

    if turtle_plr.ycor() >= 295:
        score.update_score()
        block.increase_speed()
        turtle_plr.goto(0, -280)

    for block in blocks.blocks_list:
        if block.distance(turtle_plr) < 15:
            score.game_over()
            game_is_running = False


window.exitonclick()
