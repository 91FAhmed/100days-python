import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_choice = []
user_choice = []

print("welcome to 21(BlackJack)")
print(art.logo)

def randomGen():
   computer_choice.append(random.choice(cards))
   user_choice.append(random.choice(cards))

randomGen()
randomGen()


def validate_sum():
  total_computer = sum(computer_choice)
  total_user = sum(user_choice)
  return total_computer,total_user
 
def check(total_user,total_computer):
  if(total_computer == total_user):
     return "Its a draw"
  elif(total_computer < 17):
     computer_choice.append(random.choice(cards))
  elif(total_user > 21 and total_computer < 21):
     return "Bust you loose"
  elif total_user == 21:
        return "Blackjack! You win!"
  elif(total_computer > 21 and total_user < 21):
     return "you win"
  elif total_computer == 21:
        return "Computer has Blackjack! You lose."
  else:
     return "you loose"

while True:
   total_user,total_computer = validate_sum()
   print(f"Your cards: {user_choice}, current total: {total_user}")
   print(f"Computer's first card: {computer_choice[0]}")
   if total_user >= 21 or total_computer >= 21:
        break
   ans = input("Type 'y' to hit or 'n' to hold: ").lower()

   if ans == 'y' :

       user_choice.append(random.choice(cards) ) 

   elif ans == 'n'  :

       while total_computer < 17  :

           computer_choice.append(random.choice(cards)  )

       break  

   else:  

       print("Invalid input. Please type 'y' or 'n'.")

    

total_user, total_computer = validate_sum()

print(f"Your final hand: {user_choice}, total: {total_user}")

print(f"Computer's final hand: {computer_choice}, total: {total_computer}")


# Determine the winner

result = check(total_user=total_user, total_computer=total_computer)

print(result)