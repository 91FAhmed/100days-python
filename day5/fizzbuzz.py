

target = 100
for num in range(1,target + 1):
    if(num % 3 == 0 and num % 5 == 0):
        print("fizzBuzz")
    elif(num % 3 == 0 ):
        print("fizz")

    elif(num % 5 == 0):
         print("Buzz")
    else:
        print(num)

