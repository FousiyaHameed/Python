#Python also accepts function recursion, which means a defined function can call itself.
#Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

# Generate numbers in  fibonacci sequence : 31,1,3,5,8,13..
# Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. (sum of the 2 previous numbers)
# syntax = f(n) = f(n-2) + f(n-1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n - 1) 
item_to_calculate = int(input("What fibonacci item would you like to calculate: "))
print(fib(item_to_calculate))