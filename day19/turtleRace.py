from turtle import Turtle,Screen
import turtle as globalView
import random

screen = Screen() 
screen.setup(500,400)
user_bet = screen.textinput(title="Your bet",prompt="Which turtle will win")
colors = ["red","orange","green","blue","purple"]
tim = Turtle()
turtles = []

pos_var = -100

for turtle in colors:
    new_Turtle = Turtle(shape="turtle")
    new_Turtle.color(turtle)
    new_Turtle.penup()
    new_Turtle.goto(x=-250,y=pos_var)
    turtles.append(new_Turtle)
    pos_var += 55
   
start_race = False

if user_bet != "":
    start_race = True


while start_race:
    for turtle in turtles:
        rand = random.randint(0,10)
        turtle.forward(rand)
        print(turtle.xcor())
        if round(turtle.xcor()) >= 230:
            
            start_race = False
            if turtle.color()[0] == user_bet:
                print("you won")
            else:
                print(f"You've lost your color is {user_bet}, and won is {turtle.color()[0]}")

        


globalView.exitonclick()





