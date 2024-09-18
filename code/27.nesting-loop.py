# nesting loops and conditionals
counter = 1
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1

# Controlling Loop Execution with 'continue'
print("\n")
print(" Controlling Loop Execution with 'break'  and 'continue'")
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"we are counting odd nubers: {count}")
    count += 1

# Controlling Loop Execution with 'break'
print("\n")
count = 1
while count < 10:
    if count % 2 == 0:
        break # break will stop the execution entirely
    print(f"We are counting odd numbers: {count}")
    count += 1


colors = ['blue','green','purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)


