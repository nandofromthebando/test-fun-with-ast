# A utility function that returns true if x is perfect square
import math
import logging

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


# Returns true if n is a Fibonacci Number, else false

def isFibonacci(n):
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)
#
#
# # A utility function to test above functions
for i in range(1, 15):
    if isFibonacci(i) == True:
        print('fun with ast')
        print(i, 'is a Fibonacci Number')
    else:
        print(i, 'is a not Fibonacci Number')

