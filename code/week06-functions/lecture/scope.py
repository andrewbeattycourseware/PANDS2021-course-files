# more messing with functions
# variable scope
# Author: Andrew Beatty

var = 10

def cube(num):
    #global var
    var = 66
    print ("in function var is ", var)
    return num ** 3

cube(22)
print("outside function var is ", var)
