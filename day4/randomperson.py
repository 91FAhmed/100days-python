import random

persons = ['jack','josh','angela','piperdude','alfonzo']

randomPerosn = persons[random.randint(0,len(persons) - 1)]

print(randomPerosn,len(persons)-1)