import turtle
import random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

tim = turtle.Turtle()

for _ in range (300):
 color_rand = random.choice(colors)
 tim.color(color_rand)
 tim.width(20)
 tim.speed("fastest")
  
 if _ > 50:
  tim.width(10) 
 
 tim.right(45)
 tim.forward(300)

 tim.right(160)
 tim.forward(300)



turtle.exitonclick()