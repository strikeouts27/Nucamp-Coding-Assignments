def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)


"""You are able to create a function that has itself as an parameter.

A function that calls itself is a recursive function.

A Recursive function must have a base condition that will stop 
the recursion to prevent infinite loops.
It must have a base condition or base case that can stop the recursion from going into an infinite loop. 

How to activate interactive mode:
Python -i filename.py
You can tell interactive mode is turned on when the terminal moves to >>>.
Just enter in the function name and parameter. 

Call the function by typing the name of the function and pass in the argument.
Python has a default limit of the number of recursion it allows. (100)
For example rFib(4)
if we call the function with rFib(4)
rFib(4) if called would run like this.
rFib(4) = rFib(3) + rFib(2)
rFib (3) does not meet the n ==0 or n == 1 or n ==2 so that code is run again. 
rFib (3) 3-1 and 3 - 2 creates: rFib(2) + rFib(1)
rFib(2) + rFib*(1) -> 1 + 1 = 2
this concludes line 13's rFib(3) scenario. now for rFib(2)
for rFib(2) we return 1. n == 2. we return one. So rFib equals one.
2 + 1 = 3
"""
