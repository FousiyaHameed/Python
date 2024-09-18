# Integrating 'else' with loop
count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("while loop completed")  # this statement also2 execute   

#for else
for i in [1,2,3,4,5]:
    print(i)
else:
    print("for loop completed")  # this statement also  execute  


# for else-break
colors = ['red','pink','blue','orange','green'] 

for color in colors:
    if color == 'orange':
        print("Orange is not in the list") 
        break
else:
    print("Orange is not in the list") # this statement won't execute