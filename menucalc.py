import time,sys
men = {  "Chicken Strips" : 1,
"French Fries" : 2,
"Hamburger" : 3,
"Hotdog" : 4,
"Large Drink" : 5,
"Medium Drink" : 6,
"Milk Shake" : 7,
"Salad" : 8,
"Small Drimk" : 9

}











price = {

    1 : 3.50,
    2 : 2.50,
    3 : 4.00,
    4 : 3.50,
    5 : 1.75,
    6 : 1.50,
    7 : 2.25,
    8 : 3.75,
    9 : 1.25

}

def menu():
    print("Welcome to our restaurant " + " \n Check for what you want and order it based on the number attached to the meal of your choice. Thank you")
    for key,value in men.items():
        print(key, " : ", value)
        time.sleep(1)
    
    choice = list(map(int,input("Please make your orders, space out order: \n").split()))
    total = 0
    for x in choice:
       pri =  price[x]
       total += pri
       
    print("The cost of your order is $" + str(total))

def order(): 
    while True:
        question = input("Do you want to order, please type yes or no, press q to exit"). lower()
        if question == "yes":
            menu()
            return question
        elif question == "q":
            print("Thank you for choosing us")
            sys.exit()
        else:
            print("Thank you for choosing us, maybe want to order now?")
            return question
            
    
order()