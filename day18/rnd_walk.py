import turtle
import random

tim = turtle.Turtle()
directions = [90,0,180,270]
colors  = ["red","green","blue","orange","purple","pink","yellow"]

turtle.colormode(255)


def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255);
  b = random.randint(0,255)
  return tuple((r,g,b));


def random_walk(direction):
 for c in range(200):
    rand = random.choice(direction)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(rand)
    



random_walk(directions)
turtle.exitonclick()