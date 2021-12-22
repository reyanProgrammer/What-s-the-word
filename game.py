import random
words = ["hello", "wtf", "wth", "stay", "justin-bieber", "Elon musk"]

randomchocie = words[random.randint(0, len(words)-1)]

word = input("enter your word: ")

numberofguesses = 1
limit = 3

while numberofguesses != limit:

    if word == randomchocie:
        print("you won")
        break
    else:
        numberofguesses += 1
        print("You lose")
        word = input("enter your word: ")
