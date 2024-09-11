#immutable- means something cannot be changed
#mutable- if something is mutable then it can be changed
my_str = 'testing'
my_str_cap = my_str.capitalize()

#the variable points to the exact same object. 'Testing' is new object pointing to the 
# different spot in memory. we are not modifying the object in place.if we are able to 
# modify it in place , then it's mutable type of object
print(my_str)
print(my_str_cap)

#it's going to exact same id even though the litaral that i made seperately
print(id(my_str))
print(id(id('testing')))

# creating another variable.
other_str = 'testing'
print(other_str)

#it's going to true even though they are seperate variables, because the 'testing' 
# string had already been created. because strings are immutable.it will look in the 
# exact same spot in memory.
print( id(other_str) == id(my_str))

#not all sequences are immutable. we are never going to change any string variable 
# that we have unless we have explicitely reassign the variable and at that point 
# we changing the value that the variable points to.