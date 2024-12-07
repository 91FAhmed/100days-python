import random

random_toss = random.randint(0,1)


choice = input("Heads or Tails").capitalize()
print(choice)
if(random_toss == 0):
  comp_ans = "Heads"
     
else:
     comp_ans = "Tails"

if(comp_ans == choice):
     print(f"You win {comp_ans}")
else:
     print(f"you lost comp ans {comp_ans}")