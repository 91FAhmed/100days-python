# x = 3

# new_num = int(x)

# y = 10

# z = 10.6

# print(type(new_num),type(y),type(z)) ;

# x = input("data:\n");
# print(type(x));

# first = int(x[0])
# second = int( x[1])

# print(first + second);

#PEMDAS - paranthesis exponents * / + -


#BMI

# import math
# height = input("Enter height")
# weight = input("Enter weight:")


# form = int(weight) / (float(height) *  float(height))

# print("the BMI is " + str(round(form,2)))

#f-string no need to convert

# score = 7
# danBeat = 2.1

# print(f"{score} is good is this template litral HaHAAAA!!!! Beat! {danBeat}")


# currentAge = input("enter your current Age")
# weeksinaYear = 52
# calcWeeksRemain = int(currentAge) * weeksinaYear
# weeksin90 = 4695

# print(f"your weeks {weeksin90 - calcWeeksRemain} remaining")





#final tip calc

print("welcome to tip calc")
total = input("what was the total bill amount:")
tip = input("what tip would you like to give 12 15?:")
howMany = input("how many people to split with?:")

percent = (float(total) / 100  ) * int(tip)

new_total = float(total) + percent

print(f"Each person should pay {round(new_total / int(howMany),2)}$")


