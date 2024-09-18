# Create the fizz-buzz.py Script, and Accept User Input
# Create a Range from 1 to the User's Provided Number and Loop Through It
# Print "FizzBuzz" if the Value Is a Multiple of Three and Five
# Print "Fizz" if the Value Is a Multiple of Three and "Buzz" if It's a Multiple of Five




value_limit  = int(input("How many values should we process: "))


for number in range(1,value_limit + 1 ): # if 1 to 20 , it will loop until 19 , so adding 1 to loop until 20
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
        
     
