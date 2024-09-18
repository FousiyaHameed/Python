# if we want to iterate unknown number of times or specific number of times or if we want to 
# intentionally have an infinite loop. but more common type of loop that we use in python is for loop.
# With the while loop we can execute a set of statements as long as a condition is true.

     

# Write a program to print numbers from 1 to 5 using while loop

count = 1
while count <= 5:
    print(count)
    count += 1
# Note: remember to increment count, or else the loop will continue forever.  



# Continue Statement
## With the continue statement we can stop the current iteration, and continue with the next:
print("continue statement:")
count = 0
while count < 6:
  count += 1
  if count == 3:
    continue   # # Note that number 3 is missing in the result. 
  print(count)
