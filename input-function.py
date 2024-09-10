name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

# end 
#print(name, end =" " )
#print("is " + str(age) + " years old", end = " " )
#print("and loves the color " + color + ".", end = " " )
# will get the result as  ' Aliya is 27 years old and loves the color Blue. '

print(name + " is", str(age) + " years old and loves the color "  + color + "." )
#Aliya is 27 years old and loves the color Blue.

print(name + ' is', str(age) + ' years old and loves the color ' + color + '.')
#Aliya is 27 years old and loves the color Blue.

print(name, 'is', age,'years old and loves the color',color,'.',sep=" ")
#Aliya is 27 years old and loves the color Blue .
# (when we using comma instead of '+' , it will add space after each comma(,) by default)
#   

print(name, 'is', age,'years old and loves the color',color + '.')
#Aliya is 27 years old and loves the color Blue.

print(name, 'is', age,'years old and loves the color',color + '.',sep=", ")
#Aliya, is, 27, years old and loves the color, Blue. (each word seperated by comma and space)       