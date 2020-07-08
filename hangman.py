import random
import sys
words = [ "ola",
"diana", 
"chipo",
"fiona",
"sherrie",
"funmi",
"lauren"



]

body = ["head", "shoulder", "neck", "body", "face", "knees", "toes"]




def body():
    question = input("Do you wanna play the hangman game?, Yes or no, press q to quit").strip().lower()
    if question == "yes":
        hangman()
        return question
    elif question == "q":
        sys.exit()
    else:
        print("Thank you for usimg my program")
        return question


def hangman():
    computer = words[random.randint(0, len(words)-1)]
    guess = input("Guess a letter in the word choosen by the computer?").lower
    choices = []
    for com in computer:
        if com == guess:
            print("Good choice")
            choice = body[random.randint(0, len(body)-1)]
            print("A " + choices +" has been added to the hangman")
            choices.append(choice)
        else:
            print("Try again")
            return guess

while True:

    body()