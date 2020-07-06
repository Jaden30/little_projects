
import math,time,sys
def check():
    question = input("Do you wanna do a pythagoeran triple check, enter yes/no, or press q to quit").strip().lower()
    if question == "yes":
        print("Kindly note: The third value is the opposite of the right angle, for it to be a pythagorean triple checker, the two first values should be equal to it ")
        time.sleep(3)
        a = int(input("Input your first number"))
        b = int(input("Input your first number"))
        c = int(input("Input your first number"))

        # triple checker 
        if math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
            print("Yes! you have got a Pythagorean triple. Good job")
        else:
            print("Sadly, you do not have a pythagorean triple")
    elif question == "q":
        sys.exit()
    else :
        print("Okay then. Thanks for usimg my program")
        return question

while True:
    check()