import turtle

tim = turtle.Turtle()


def draw_shape(number):
    rotation = 360 / number
    for _ in range(number):
     tim.forward(100)
     tim.right(rotation)
    


for shapes_n in range(3,11):
    draw_shape(shapes_n)

turtle.exitonclick()