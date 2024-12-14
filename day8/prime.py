

def is_prime(number):
  prime = True
  for i in range(2,number):
    if(number % i == 0):
      prime = False
  if(prime):
      print("its a prime")
  else:
      print("not a prime")

n = int(input())
is_prime(number=n)

