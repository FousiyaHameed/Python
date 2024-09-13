my_list = [1,2,3,4,5]
print(my_list)

other_list = ['a',2,1.0,False]
print(other_list)

print(my_list[0])
print(my_list[3])
#print(my_list[16])# list index out of range(we get the similar error indexing into a string)

print(len(my_list)) # 5

# when we would slice a string we would get a string back and when we slice a list will get a list back
print(my_list[0:2]) #[1, 2]
print(my_list[1:]) #[2, 3, 4, 5]

#stepping also works
print(my_list[0::1])  # standard stepping by one, [1, 2, 3, 4, 5]
print(my_list[0::2])  #[1, 3, 5]

# list are mutable type means we can modify them
#modifying the list in place
my_list[0] = 'a'
print(my_list) #['a', 2, 3, 4, 5]

#concatenateca a list, return a new list
print(my_list+[7,8,9])# ['a', 2, 3, 4, 5, 7, 8, 9]
print(my_list) #['a', 2, 3, 4, 5]

# creating a new list by reassigning the list
my_list += [7,8,9] # my_list = my_list + [7,8,9]
print(my_list) #['a', 2, 3, 4, 5, 7, 8, 9]

# reassigning the list(my_list)by assigning a new list to the slice
my_list[1:3] = ['b', 'c'] 
print(my_list)  #['a', 'b', 'c', 4, 5, 7, 8, 9]

my_list[3:5] = ['d','e','f']
print(my_list) #['a', 'b', 'c', 'd', 'e', 'f', 7, 8, 9]

# can remove items from the list
# reset the list
my_list = ['a','b','c','d',5,6,7]
my_list[4:] = [] # removing items by assigning an empty list to the slice
print(my_list) #['a', 'b', 'c', 'd']

#more common way to remove items from the list is by using del statement which stands for delete
del my_list[0]
print(my_list) #['b', 'c', 'd']

#if you forgot to do the index, it will completely remove the list entirely.
del my_list
# so the now the e varible itself doesn't even exist. it's as we never assigned  anything to the my_list variable
print(my_list) #NameError: name 'my_list' is not defined