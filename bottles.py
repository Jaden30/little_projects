
def bottles():
    for x in range(99, -1, -1): 
        if x == 1:
            print(str(x) + " bottle of beer on the wall, " + str(x) + " bottle of beer om the wall" + "\n take one dowm")
        elif x == 0:
            print("No more bottles on the wall No more bottles on the wall \n Go to the store and buy more")
        else:
            print(str(x) + " bottles of beer on the wall, " + str(x) +" bottles of beer on the wall " + " \n take one down")

bottles()