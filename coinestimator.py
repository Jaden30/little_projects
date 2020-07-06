# comvert gram to pound 

weights = {'penny': 2.5, 'nickel': 5, 'dime': 2.268, 'quarter': 5.67, 'half dollar': 11.34, 'dollar': 8.1}
rolls =  {'penny': 50, 'nickel': 40, 'dime': 50, 'quarter': 40, 'half dollar': 20, 'dollar': 25}
worths = {'penny': .01, 'nickel': .05, 'dime': .10, 'quarter': .25, 'half dollar': .50, 'dollar': 1.00}

def coin():
    type = input("What type of coins do you have?").strip().lower()
    weight_type = input("Do you want to use pounds or grams?").strip().lower()
    weight = float(input("The total weight of each type of coin you have"))
    

  
    if weight_type == "lb" or weight_type == "g":
        if type in weights:
            coinRoll = round(weight/ weights[type])
            rollSize = round(coinRoll/rolls[type])
            worth = round(coinRoll * worths[type])
            print("You are advised to use the " + str(rollSize) + str(weight) + "\n This is because you have "  + str(coinRoll) + " rolls and it is worth " + str(worth))
        else:
            print( "I am sorry, we cam not give you an accurate estimate ")
    else:
        print("Incorrect weight, please pounds(lb) or gram(g)")
coin()