#Create the ~/to-celsius.py Script 
#Prompt and Store Fahrenheit Value from User
#Calculating the Celsius Value
#Print the Calculated Value to the Screen
fahrenheit = float(input("what temperature (in fahrenheit) would you like to converted to celsius? "))

#Calculating the Celsius Value
#The Fahrenheit to Celsius formula is celsius = (temp - 32) * 5 / 9 and this converts almost perfectly to Python. 
# We only need to change temp to be our variable fahrenheit.
celsius = (fahrenheit - 32) * 5/9

#Print the Calculated Value to the Screen in the form of:FAHRENHEIT F is CELSIUS C
print(fahrenheit , "F is", round(celsius,2),"C")





