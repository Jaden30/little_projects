import math,sys

def change():

    while True:
        total = float(input("How much did the customer pay"))
        cost = float(input("How much was his goods worth?"))

        change = total-cost

        if change < 0:
            print("Customer needs to give you the balance, money not complete!")
        elif change == 0:
            print("No change needed, thank customer for coming")
            sys.exit()
        else:
            # calculate the change 
            pound = math.floor(change/1)
            change = round(change- pound *1,2)
            fiftypence = math.floor(change/.50)
            change = round(change-fiftypence*.50,2 )
            twentypence = math.floor(change/.20)
            change = round(change-twentypence*.20,2)
            twopence = math.floor(change/.02)
            change = round(change-twopence*.02,2)

            #change to be given 
            if change == 0:
                print("Give customer " + str(pound)  + str(fiftypence)+ str(twentypence) + str(twopence)+ "Thank the customer for coming")
            else:
                print("There is something wrong")
            
change()