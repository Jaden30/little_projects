
from random import randint
import sys


print("The game involves you guessing a number that the computer already guessed, if you get the number guessed you win")

def game():
    while True:
        random =randint(1,100)
        # empty list to check the number of tries 
        list_guess = []
        # input to guess a number
        guess = int(input("Guess a number, or press q to exit"))
        # append the list 
        list_guess = list_guess.append(guess)
        # conditional statement to check the number of guesses
        if guess == random:
            print("Congratulations that was a good guess" )
            print("The number of guesses it took you to get here is " + len(list_guess))        
        elif guess == "q":
            sys.exit()
        elif guess < random:
            print("Your guess is lower than the actual number")
        else:
            print("Your guess is higher than the number")
        
        
      
        
       
while True:


    game()
    