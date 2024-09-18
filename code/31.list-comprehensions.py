#List Comprehensions
# Covert the list of colors to uppercase list

colors = ['red','blue','yellow','pink','green','purple','orange']
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())
print(uppercase_colors) # result will be ['RED', 'BLUE', 'YELLOW', 'PINK', 'GREEN', 'PURPLE', 'ORANGE']   


#we can do the same with a single line of code
print("by using list comprehensions- uppercase colors")
colors = ['red','blue','yellow','pink','green','purple','orange']
uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors,"\n")
# we will get the same result; ['RED', 'BLUE', 'YELLOW', 'PINK', 'GREEN', 'PURPLE', 'ORANGE']

# to get warm colors from the list
print("warm colors")
warm_colors = []
for color in colors:
    if color in ['red','orange','yellow']:
        warm_colors.append(color)
print(warm_colors)

# we could achieve the exact same thing
print("\n")
print("by using list comprehensions- warm colors")
warm_colors = [color for color in colors if color in ['red','orange','yellow']]
print(warm_colors)