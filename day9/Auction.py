import gavelArt

print("Welcome to python Auction")
print(gavelArt.gavel)

is_there = "yes"
recipients_info = []

def AssignValue(name,amount):
 newPerson = {}
 newPerson['name'] = name
 newPerson['amount'] = int(amount)
 recipients_info.append(newPerson)

winner = ""

def Validify():
 highest = 0
 global winner
 for person in recipients_info:
  if(person['amount'] > highest) :
   highest = person['amount']
   winner = person['name']
  else:
   print("enter valid STRING ONLY")  
  
 

while((is_there).lower() == "yes"):
 person = input("Enter the Recipients Name:")
 amount = input("Enter the amount")
 is_there = input("is there any other person yes or no")
 AssignValue(name=person,amount=amount)
 Validify()

print(f"the winner is {winner}")


