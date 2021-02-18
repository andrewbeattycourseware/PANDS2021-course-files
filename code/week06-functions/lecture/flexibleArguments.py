# More messing with functions
# flexible arguments
# Author: Andrew Beatty

print ("hi", 55, 343, [], {}, sep=":")

# flexible number of arguments

def average(*numbers):
    sumOf = sum(numbers)
    return sumOf / len(numbers)


ave = average (12, 12, 12, 34,12,34)
print ("average is ", ave)


# flexible number or named arguments

def fun(arg1 = 0, arg2 = 1 ):
    return arg1 - arg2

print (fun(arg2 = 10, arg1 = 2))

def funkyArgs(**args):
    print (args)

funkyArgs(name="joe", age = 33, courses = [])