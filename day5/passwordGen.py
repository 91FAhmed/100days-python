
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


alphabets = []
rnd_char = []
rnd_symbol = []
rnd_number = []
rnd_letter = 0
# print(len(letters))
for letter in range(0,len(letters)):
#letter - index
 if(len(rnd_char) < nr_letters ):
  rnd_letter = random.randint(0,len(letters) - 1)
  rnd_char.append(letters[rnd_letter])
 else:
   print("letter out of range (0 - 25)")
#letters[letter]
 if(len(rnd_symbol) < nr_symbols):
    rnd_symbol.append(symbols[letter])
 else:
   print("symbols out of range (0 - 8)")
 if(len(rnd_number) < nr_numbers):
   rnd_number.append(numbers[letter])
 else:
    print("number out of range (0 - 9)")

 
finalPass = []

print(rnd_letter)
length = 0
for i in rnd_char,rnd_symbol,rnd_number:
  length = int(nr_letters) + int(nr_numbers) + int(nr_symbols)

finalPass = rnd_number + rnd_char + rnd_symbol
random.shuffle(finalPass)
res = ''.join(finalPass)
  
print(res)