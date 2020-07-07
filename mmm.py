import math
#using sorted and a list comprehension to take the input 
numbers = sorted([int(x) for x in input("A list of numbers, seperated by ,").split(",")])
print(numbers)
def mean():
    
    sig = int(input("You want your answer to be rounded to how many significant number?"))
    total = 0
    for no in numbers:
        total += no

    mean = round(total/ len(numbers),sig)
    print("The mean is " + str(mean) )

def median():
    # checking the length in numbers
    length = len(numbers)
    # conditional statement to check for the method to use to obtain the median
    if length % 2 == 0:
        middle = (numbers[int(length/2 -1)] + numbers[int(length/2)])/ 2
        
    else:
         middle = numbers[int(length/2)]
        
    print("The median is " + str(middle))
    

def mode():
    # creating an empty dictionary
    dictionary = {}
    count = 0
    for no in numbers:
        # to check the number of times it appears in a list 
        count = numbers.count(no)
        # to store it in a dictionary
        dictionary[no] = count
  

    # a function to check for the maximum value in a dictionary 
    maximum = max(dictionary.values())
    if maximum == 1:
        print("A maximum can not be obtained as all values appear only once")
    else:
        res = [ key for key in dictionary if dictionary[key] == maximum]
        print("The mode is " + str(res))
   
        
            
 

mean()
median()
mode()
