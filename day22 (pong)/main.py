from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# Paddle class
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
score_b = ScoreBoard()

paddle_l.create_paddle()
paddle_r.create_paddle()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Atari")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_b.r_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_b.l_point()


screen.exitonclick()
