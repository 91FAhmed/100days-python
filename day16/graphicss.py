from turtle import Turtle,Screen

turt = Turtle()
print(turt)

screen = Screen()
print(screen.canvwidth)
print(screen.canvheight)
turt.shape("turtle")
turt.right(45)
turt.forward(300)
turt.right(90)
turt.forward(200)
turt.right(90)
turt.forward(200)
turt.right(90)
turt.forward(300)
turt.left(135)
turt.forward(130)

turt.color('#285078')
screen.exitonclick()
