from turtle import Turtle, Screen
from turtleplay import TurtlePlayer
from blocks import Blocks
import time

# Creating Screen
window = Screen()
window.setup(600, 600)
# turning animation off
window.tracer(0)
# Create turtle
turtle_plr = TurtlePlayer()
block = Blocks()

game_is_running = True

window.listen()

window.onkey(turtle_plr.move_up, "space")

while game_is_running:
    window.update()
    Blocks().random_move()
    Blocks.move()
    time.sleep(0.1)


window.exitonclick()
