import math
number = input("Please input a digit").strip()
length = len(number)
print(length)
added = 0
for x in number:
    num = number.index(x)
    #added = added + math.pow(num, length)
print(num)