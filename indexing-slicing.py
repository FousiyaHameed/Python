test_str = 'testing'
# to get individual item in a string
print(test_str[0]) # result will be 't'
#print(test_str[18])#indexError:string index out of range
print(test_str[len(test_str)-1]) #negative indxing, will get result as 'g'
print(test_str[-1])# will get the result as 'g'

# slicing is used to specify range of index to work with
print(test_str[0:2]) # 'te'
print(test_str[3:5]) # 'ti'
print(test_str[2:len(test_str)])#'sting', the value returning outside of the bounds of string
#because index start with 0, still it work even the index doesn't exist, this is not the way 
# you are going to do it, because we have short hand for it. 

# to start with an index and go with the end of the string
print(test_str[2:])


# full way of slicing [starting index:ending index:step value]
print(test_str[1:5:2])  #  will get the result as 'et' by slicing the 'testing' string
print(test_str[1:6:2]) # ''etn' 
print(test_str[:6:2]) # to start with the begning of the string and result will be'tsi'

#from a specific point to all the way to the end using a step value
print(test_str[1::2]) # 'etn' 

#slice with negative step value; this is one way we can reverse a string.
# The default step value is one
print(test_str[::-1]) # 'gnitset'
