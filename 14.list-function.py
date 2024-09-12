# List functions and methods

my_list = [1,2,3]
my_list.append(4) # add item to the list
print(my_list) #[1, 2, 3, 4]

# adding item to the specified index and it doesn't replace the item
my_list.insert(0,'a')
print(my_list) #['a',1, 2, 3, 4]

# to know the actual position of an item in the list ,use the index method
my_list = [5,10,15,20]
print(my_list.index(15)) # 2

# will get value error if we try to find an item that doesn't exist in the list
#print(my_list.index(17)) #ValueError: 17 is not in list

# in and not in operation
my_list = [1,2,3]
print(4 in my_list) # False
print(4 not in my_list) #True
print(2 in my_list) #True
# based on this we can then determine if we want it to go look for the index 
# and we would know whether or not it was going to give an error because if
# 4 in my_list return False, then we know it's always give us an error 
# when we try to index the list to know the position of the item 4.

# To sort the list using sorted function
my_list = [5,1,7,3,6,2,4,]
print(sorted(my_list)) #[1, 2, 3, 4, 5, 6, 7]

# we can't use the reversed in the similar way of sorted function syntax.
print(reversed(my_list)) # returns list_reverseiterator object

#To reverse the list use list function
# reverse the list [5,1,7,3,6,2,4,]
print(list(reversed(my_list))) #[4, 2, 6, 3, 7, 1, 5]

#reverse the sorted list [1, 2, 3, 4, 5, 6, 7]
print(list(reversed(sorted(my_list))))