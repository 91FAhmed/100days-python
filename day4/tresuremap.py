
         #A   #B  #C
line1 = [" "," "," "] #1
line2 = [" "," "," "] #2
line3 = [" "," "," "] #3

map = [line1,line2,line3]

position = input("where to store B1 B2 B3 A1 etc:")
xaxis = position[0]
yaxis = position[1]

xnumber = 0

if(xaxis == str('B')):
  xnumber = 1
elif(xaxis == str('A')):
   xnumber = 0
else:
   xnumber = 2

print(xnumber)

map[int(yaxis) - 1][xnumber] = "x"

print(f"{map[0]}\n{map[1]}\n{map[2]}")