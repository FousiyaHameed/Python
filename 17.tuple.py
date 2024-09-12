#Immutability: One of the key differences between tuples and other 
# Python data structures is that tuples are immutable. Once a tuple 
# is created, its contents cannot be changed. In contrast, lists and 
# dictionaries are mutable, meaning that their contentscan be modified after 
# they are created. 

point = (1.0,2.0)
# point[0] = 1 #TypeError: 'tuple' object does not support item assignment
print(point)

#if we add (4.0) instead of (4.0,) will get error 
#point_3d = point + (4.0) #TypeError: can only concatenate tuple (not "float") to tuple
point_3d = point + (4.0,)
print(point_3d) # (1.0, 2.0, 4.0)

x,y,z =  point_3d

print(x) #1.0
print(y) #2.0
print(z) #4.0

print("My name is: %s %s" % ("Keith","Thompson"))#My name is: Keith Thompson


person = ('kevin Bacon',61,"555-555-555")
person2 = ('Bob Ross',76,"")
print(person[0])
print(person2[0]) 

my_list = [1,2,3]

# list in tuple
my_tuple = (my_list,1)
print(my_tuple) #([1, 2, 3], 1)

# tuple in list
other_list = [1,2, my_tuple]
print(other_list) #[1, 2, ([1, 2, 3], 1)]

# add an item to the end of the list
my_list.append(5)
print('added an item to the existing list',my_list)

# tuple cannot be modified ,but list can be modify
# list can be in tuple.Tuples can be in lists.
# if you modify list in tuple, it will not broke the tuple.it will still modify the list that's in there.
# tuple is immutable.
print(my_tuple)   # ([1, 2, 3, 5], 1)
print(other_list) # [1, 2, ([1, 2, 3, 5], 1)]