
import random,sys
options = [
    "rock",
    "paper",
    "scissors"
]

player_score = 0
computer_score = 0
   
player_choice = ""
computer_choice = "" 
def game(player_choice, computer_choicet, computer_score, player_score):
        
        
    while True:

        player_choice = input(" Choose between rock, paper and scissors").lower().strip()
      
        if player_choice not in options:
            print("Error, choose between rock, paper or scissors")
        else:
            computer = options[random.randint(0, len(options)-1)]
            computer_choice = computer
            print("player choice is " + player_choice + " and computer_choice is " + computer_choice)
            
    # returning certain numbers     
            if player_choice == computer_choice:
                print("Good game is a draw ")
            elif player_choice == "rock" and computer_choice == "scissors":
                print("You win")
                player_score = +1
            elif player_choice == "paper" and computer_choice == "scissors":
                print("Computer win")
                computer_score = +1
            elif player_choice == "scissors" and computer_choice == "paper":
                print("You win")
                player_score = +1
            elif player_choice == "rock" and computer_choice == "paper":
                print("Computer win")
                computer_score = +1
            elif player_choice == "scissors" and computer_choice == "rock":
                print("Computer win")
                computer_score = +1
            elif player_choice == "paper"  and computer_choice == "rock":
                print("You win")
                player_score = +1
            else:
                print("invalid game")
            
   
            if computer_score > player_score:
                print("The score of the game for the computer is " + str(computer_score) + "The score of the game for the player  is " + str(player_score) + " computer wins")
            elif computer_score == player_score:
                print("The score of the game for the computer is " + str(computer_score) + "The score of the game for the player is " + str(player_score) + "It is a draw")
            else:
                print("The score of the game for the computer is " + str(computer_score) + "The score of the game for the player is " + str(player_score) + "You win")
def keepplaying():
   while True:
        question = input("Do you wanna play Rock, paper and scissors?, Answer yes or no, press q to exit").lower().strip()
        if question == "yes":
            game(player_choice,computer_choice, computer_score, player_score)
            return question
        if question != "yes" or question != "no":
            print("invalid response, try again")
            return question
        if question == "q":
            sys.exit()
keepplaying()