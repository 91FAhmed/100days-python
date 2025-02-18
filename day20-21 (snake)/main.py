from turtle import Turtle, Screen, write
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
Score = ScoreBoard()


screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    Score.sc_board()

    if snake.head.distance(food) < 15:
        food.update()
        snake.extend()
        Score.update_score()

    # wall collision
    if (
        round(snake.head.xcor()) >= 295
        or round(snake.head.xcor()) <= -295
        or round(snake.head.ycor()) >= 295
        or round(snake.head.ycor()) <= -295
    ):
        game_is_on = False
        Game = GameOver()

    # Body parts collision
    for parts in snake.body_parts[2:]:
        if snake.head.distance(parts) < 10:
            game_is_on = False
            GameOver()

screen.exitonclick()
