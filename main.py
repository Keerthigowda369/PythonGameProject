import random
import time

a = ["student", "regional", "distinct", "hypothesis", "pseudo code", "psychology", "scissors", "percentage",
     "terrorism", "national", "average", "avengers", "horizontal", "vertical", "diagonal", "global", "supernova",
     "apple", "table", "cricket", "football", "tennis", "hockey", "table tennis", "chess", "carroms", "movie", "story",
     "animal", "human being", "elephant", "tiger", "crocodile", "horse", "buffalo", "donkey", "monkey", "random",
     "combine", "permutation", "examine", "determine", "alien", "time travel", "black hole", "worm hole", "interstellar",
     "adventure", "disaster"]
x = a[random.randrange(0, len(a))]
y = []
guess_count = 0
for i in x:
    if i == " ":
        y.append(" ")
    else:
        y.append("_")
word = "You will get 20 chnance to guess the correct word.\nEnter any letter to find if it is present in the given word.\nIf you have guessed the word, \nEnter: ans followed by your word\nFor example if you got that the answer is mango then type like it is typed below\nans mango\n"
for letter in word:
    print(letter,end="")
    time.sleep(0.05)
print(*y, sep=" ")
print("Type a single to start the game\n")
while 1 and guess_count<20:
    key = input("").lower()
    guess_count+=1
    print("You have ",20 - guess_count," attempts left")
    if key[:4] == "ans ":
        if key[4:] == x:
            print("Solved!!")
            break
        else:
            print("Wrong answer!")
            continue
    if len(key) > 1 or key.isalpha() != True:
        print("Enter a valid key")
        print("You have ",20 - guess_count," attempts left")
        guess_count-=1
        continue
    for i in range(len(x)):
        if y[i] != "_":
            print(y[i], end=" ")
        elif x[i] == key:
            y[i] = key
            print(y[i], end=" ")
        else:
            print(y[i], end=" ")
    print("")
    if y == list(x):
        print("Solved!")
else:
    print("You Lost :(")
    print("The word was ",x)