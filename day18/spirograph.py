import turtle as t
import random

tim = t.Turtle()

t.colormode(255)
tim.speed("fastest")
def rand_color():
 r = random.randint(0,255)
 g = random.randint(0,255)
 b = random.randint(0,255)
 return tuple((r,g,b))

for _ in range(200):
 tim.color(rand_color())
 tim.circle(100)

 tim.setheading(_ * 10)
 



t.exitonclick()