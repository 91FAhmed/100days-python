import random

# Rock
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors =  ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

collectionOfAscii = [Rock,Paper,Scissors]

choice = input('enter your choice ''0'' for rock ''1'' for paper or ''2'' scissors:')

score = 0
compScore = 0

if(int(choice) <= 2):
 if(choice == str(0)):
    print(Rock)
 elif(choice == str(1)):
    print(Paper)
 else:
    print(Scissors)
else:
   print("enter between 0 to 2 only")

#computer
print('computer choice')
comp_choice = random.randint(0,2)

print(collectionOfAscii[comp_choice])

if(comp_choice == 0 and choice == str(1)):
  print("You win")
  score += 1

elif(comp_choice == 0 and choice == str(2)):
   print("you lose")
   score += 1
elif(comp_choice == 1 and choice == str(0)):
   print("you lose")
   compScore += 1
elif(comp_choice == 1 and choice ==str(2)):
   print("you win")
   score += 1
elif(comp_choice == 2 and choice == str(1)):
   print("You lose")
   compScore += 1
elif(comp_choice == 2 and choice == str(0) ):
   print("you win")
   score += 1
else:
   print("draw")