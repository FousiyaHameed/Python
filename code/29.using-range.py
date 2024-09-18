#if you want to iterate certain number of time, we can use the range function
my_range = range(10) # start and stop value can specify

print(my_range) #range(0,10)
print(list(my_range)) # [0,1,2,3,4,5,6,7,8,9]

# full way of creating range
# start value,stop value and step value, this is exact same way that we worked  with slices
print(list(range(1,14,2))) #[1, 3, 5, 7, 9, 11, 13]

print("\n")
print("while loop without range function")
count =1
while count <= 4:
    print("looping")
    count += 1

# not needed to worry about incrementing a counter otr potentially falling to an infinte loop by using range function.

print("\n")
print("for loop with range function")
for _ in range(4):
    print("looping")
