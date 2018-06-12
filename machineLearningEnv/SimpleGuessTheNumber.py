import os
import random

def main():
    print "The number game"
    print "Guess a number between 0 and 200"

    userName = raw_input("What's your name?: ")

    randomNumber = random.randrange(200)
    userGuess = ""

    messagesFile = open("motivation.txt", "r")
    motivationList = messagesFile.read().splitlines()
    messagesFile.close()

    userMotivations = map(lambda motivation: "** " + motivation + ", " + userName + "! **", motivationList)
    while userGuess != randomNumber:
        userGuess = int(raw_input("Your guess:"))

        if userGuess < randomNumber:
            print random.choice(userMotivations)
            print "Too low"
        elif userGuess > randomNumber:
            print random.choice(userMotivations)
            print "Too high"
    print "Correct!"

    raw_input()

main()
