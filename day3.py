# ans = int(input("enter your height"))

# if ans > 120:
#   print("You can ride")
# else:
#   print("you cant")

# check odd or even

# data = int(input("enter the value"))

# if(data % 2 == 0):
#     print("The number is even")
# else:
#     print("the numbrt is  odd")

# upgraded BMI
# height = input("Enter height")
# weight = input("Enter weight:")
# form = int(weight) / (float(height) * float(height))
# BMI =  round(form, 1)


# if(BMI < 18.5):
#      print(f"your bmi is {BMI} is underweight")
# elif(BMI >= 18.5 and BMI <= 25):
#       print(f"your bmi {BMI} has normal weight")
# elif(BMI > 25 and BMI <=30 ):
#          print(f"your bmi {BMI} has slight overweight weight")
# elif(BMI > 30 and BMI <=35 ):
#          print(f"your bmi {BMI} has clinically obeseity weight")
# else:
#  print(f"your bmi {BMI} has clinically obeseity weight")

#leap or not

# print("The leap year detector")
# year = int(input("Enter the year"))

# if(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
#      print(f"year {year} is a leap year")
# else:
#     print(f"year {year} is not a leap year")


#pythonPizza

# size = input("enter the pizza size S,M,L")
# addpep = input("add peporoni Y or N")
# extra_cheese = input("add extra cheese Y/N")

# bill = 0

# if(size == 'S'):
#     bill += 15
# elif(size == 'M'):
#      bill += 20
# else:
#      bill += 25
    
# if(addpep == 'Y'):
#     if(size == 'S'):
#        bill += 2
#     elif(size == 'L' or size == 'M'):
#         bill += 3

# if(extra_cheese == 'Y'):
#     bill += 1

# print(f"your total bill is {bill}$")

# print("love calculator")

# hostName = input("Enter your name:")
# clientName = input("Enter client name:")


# T = hostName.lower().count("t")
# R = hostName.lower().count("r")
# U = hostName.lower().count("u")
# E = hostName.lower().count("e")

# print(f"T occurs {T}")
# print(f"R occurs {R}")
# print(f"U occurs {U}")
# print(f"E occurs {E}")

# TC = T + R + U + E
# print(f"total time {TC}")

# L = hostName.lower().count("l")
# O = hostName.lower().count("o")
# V = hostName.lower().count("v")
# E = hostName.lower().count("e")

# print(f"L occurs {L}")
# print(f"O occurs {O}")
# print(f"V occurs {V}")
# print(f"E occurs {E}")

# LC = L+O+V+E

# print(f"total time {LC}");

# print(f"Your score is {str(TC) + str(LC)}")


print('''     _      _      _      _      _      _      _
   _( )__ _( )__ _( )__ _( )__ _( )__ _( )__ _( )__
 _|     _|     _|     _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _) _   _) _   _) _   _)
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
 _|     _|     _|     _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _) _   _) _   _) _mx _)
 |__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|__( )_|''')

print("welocme to tresure island")
ans = input("which door red or blue or yellow\n").lower()
if(input("left or right\n") == "right"):
     print("game over")
elif(input("swim or wait\n") == "swim"):
    print("game over")
    
elif(ans == "blue" or ans == "red"):
    print("game over")
    
else:
     print("you win")