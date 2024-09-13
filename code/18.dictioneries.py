#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and 
# do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values

ages = {'kevin':59,'alex':29,'bob':40}
print(ages)
#print(ages['billy']) # KeyError: 'billy';because the key does not exist the key
print(ages['kevin'])

#we can add item to dictionary
ages['kayla'] = 21
print(ages)

# we can reassign values
ages['kevin'] = 60
print(ages)

#remove the key from the dictionery
del ages['kevin']
print(ages)

# use of in and not in dictioney
print('kevin' in ages) # False
print('kevin' not in ages) #True
print('alex' in ages) #True

#different way to create dictionary
weights = dict(kevin = 90,bob = 100,kayla = 70)
print(weights)

#another way of creating dictionary by passing list of tuples
colors = dict([('kevin','blue'),('bob','green'),('kayla','red')])
print(colors)

#dictionary methods
ages = {'kevin': 61, 'bob': 79}
print(ages.keys()) # return keys
print(list(ages.keys())) # return keys in a list 

#to get values of the key
print(ages.values())
print(list(ages.values())) # return values in a list 

# item will give key and values
print(ages.items()) #list of tuples
print(list(ages.items())) 