from turtle import Turtle, Screen
from paddle import paddle


# Paddle class
paddle_l = paddle((-350, 0))
paddle_r = paddle((350, 0))

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Atari")
screen.tracer(0)

paddle_l.create_paddle()
paddle_r.create_paddle()

screen.listen()
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
