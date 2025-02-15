import turtle as tex

tim = tex.Turtle()

def move():
    tim.forward(20)

def back():
   tim.backward(20)

def left():
    tim.left(90)

def right():
   tim.right(90)

tex.listen()
print(tex.listen())

tex.onkeypress(move,'w')
tex.onkeypress(left,'a')
tex.onkeypress(right,'d')
tex.onkeypress(back,'s')



tex.exitonclick()