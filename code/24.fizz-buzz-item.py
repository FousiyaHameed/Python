#Create the fizz-buzz-item.py Script, Make It Executable with python3.7, and Accept User Input


#Print "FizzBuzz" if the Value Is a Multiple of Three and Five
#Print "Fizz" if the Value Is a Multiple of Three, and "Buzz" if it's a Multiple of Five

value = int(input("Enter an integer value: "))

if value % 3 == 0 and value % 5 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz") 
elif value % 5 == 0:
    print("Buzz")
else:
    print(f"The entered value {value} is not evenly divisible by 3 or 5")