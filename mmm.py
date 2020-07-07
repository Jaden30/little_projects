import math
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
    length = len(numbers)
    if length % 2 == 0:
        middle = (numbers[int(length/2 -1)] + numbers[int(length/2)])/ 2
        
    else:
         middle = numbers[int(length/2)]
        
    print("The median is " + str(middle))
    

def mode():
    dictionary = {}
    count = 0
    for no in numbers:
        count = numbers.count(no)
        dictionary[no] = count
    print(dictionary)

    
    maximum = max(dictionary.values())
    if maximum == 1:
        print("A maximum can not be obtained as all values appear only once")
    else:
        res = [ key for key in dictionary if dictionary[key] == maximum]
        print("The mode is " + str(res))
   
        
            
 

mean()
median()
mode()
