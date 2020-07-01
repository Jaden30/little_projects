# importing time and random module to use for the question and games 

import time, random
import sys 
# responses for the question that would be asked at random
responses = [
    " You are wasting my time",
    " Ask a better question",
    "What are you trying to achieve?",
    " I do not know that one",
    " I do not know what you mean",
    "  I am not gonna answer that"
    "Be better"
]



def question():
    input("Ask a question??")

    print("I am thinking")
    time.sleep(6)

    respond = responses[random.randint(0, len(responses)-1)]
    print(respond)
    time.sleep(5)

while True:
    # to keep the game running
    question()
  

    quit = input("Press q if you wanna quit ")

    if quit == "q":
        sys.exit()