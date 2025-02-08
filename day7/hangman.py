import random
wordList = ["beekeeper"]
# "cowboy","netherlands"


random_word = random.choice(wordList)

random_len = len(random_word)
life = random_len
list = []

guessed_word =  input("guess the Word")
end = False
while not end:
 for _ in range(0,random_len):
    list += "_"
    if(random_word[_] == guessed_word):
        list[_] = guessed_word
    else:
        life -= 1
   

    if "_" != list:
        end = "true"
        print("you win")




