import art
import dataList
import random


def random_selector(data):
   return random.choice(data)

score = 0

while True:
 print(art.logo)
 a = random_selector(data=dataList.data)
 print(f"compare A:{a['name']} a {a['description']} ")
 
 
 print(art.vs)
 
 
 b = random_selector(data=dataList.data)
 print(f"compare B:{b['name']} a {b['description']}")
 print(a['follower_count'],b['follower_count'])
 answer =  input("who has more followers A or B").lower()
 if(answer == "a"):
   if(a['follower_count'] > b['follower_count']):
     print("you are correct")
     score += 1
   else:
     print(f"You are wrong total score:{score}")
     break
 else:
    if(b['follower_count'] > a['follower_count']):
     print("you are correct")
     score += 1
    else:
     print(f"You are wrong total score:{score}")
     break


