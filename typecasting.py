print(float(1)) # converting integer to float
print(int(1.3)) # converting integer to float
print(str(1)) # converting integer to string
print(str(1.0)) # converting float to string
print(str(False)) # converting boolean to string
print(int('1')) # converting string to integer
print(float('1')) # converting string to float
print(float('1.2')) # converting string to float
#print(int('1.2')) # converting string to integer, will get valueerror
#1.2 is not an integer literall , so we can't convert it to integer.

print(bool(1)) # return True
print(bool(2.4)) # return True
print(bool('Tada')) # return True
#everything has true and false representaton, almost evrything is going to be true boolean value
#with the exception of very specific things
print(bool(0)) # return False
print(bool(0.1)) # return False
print(bool('')) # return False
print(1 and 0) # return False; 
# it takes look on the leftmost one, it is true then looks on the right it is false, so return false.
print('This' and 'That') # return False
print('This' and 0 and 'That') #return 0, returns the first falsy value or returns the last truthy value.

print(0.0 and 1) # returns 0.0, if the value start with falsy value then it retuns falsy value.

print(1 or 0) # return 1
print(0 or 1) # return 1
print(0 or "") # return '', these both false and returns last falsy value
print(0 or 1 or 'This') # returns 1, returns fist true value

print(not "") # return True
print(not bool("")) # return True
print(not 1) # return False



