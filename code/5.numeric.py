# numeric operators

print(2 + 2)
print(2.0 + 2.0)
print(2.0 + 2) # one is float other one is integer and it is always return a float, if a float was involved in the operation.
print(3 * 9)
print(5 / 3) # standard division. Always gives float result even it is evenly divisible.
print(10/2) # 5.0

#In Python, we can perform floor division (also sometimes known as integer division) using the // operator. 
# This operator will divide the first argument by the second and round the result down to the nearest whole number,
#  making it equivalent to the math. floor() function.
print(5 // 3) # 1
print(10 // 2) # 5

# will give the whole number reminder.
print(5 % 3) # 2

 # % useful  to determine if something is evevn or odd
print(12 % 2) # return 0 (wehen the results zero it means the number is even ) 
print(13 % 2)# return 1 (wehen the results one it means the number is odd )

#exponent
print(2 ** 3) # it is equal to 2*2*2   will get 8
