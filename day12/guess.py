import random

print("Welcome to random number Guessing game")
print("think of a number from 1 to 100")

difficulty_level = input("Choose a difficulty 'easy' or 'hard':").lower()



def random_gen():
 return random.randint(1,100)



def validate(secret,user_no):
    if(int(user_no) == secret):
          return "you win"
    elif(int(user_no) > secret):
       return "too high"
    else:
        return "too low"
   
   



if(difficulty_level == 'hard'):
    SECRET_RAND =  random_gen()
    print("you'll have only 5 lives")
    live = 5
    while live > 0:
     print(f"You have {live} remaining")
     user_no = input("Make a guess")
     ans = validate(secret=SECRET_RAND,user_no=user_no)
     print(f"{ans}")
     if live == 1:
        print("you failed")
     live -= 1
     
elif(difficulty_level == 'easy'):
    SECRET_RAND =  random_gen()
    print("you'll have only 10 lives")
    live = 10
    while live > 0:
     print(f"You have {live} remaining")
     user_no = input("Make a guess")
     ans = validate(secret=SECRET_RAND,user_no=user_no)
     print(f"{ans}")
     if live == 1:
        print("you failed")
     live -= 1

else:
   print("Enter a valid string 'hard' or 'easy'")