# Defining and Using Functions

#defining function
def print_name(name):
    print(f"Name is {name}")


#calling function
print_name('Arman')

# we need to return a value after calling  a function to save the value into a variable
def add_two(num):
    return num + 2
result = add_two(2)
print(result)

# multiple parameters
def add(num1,num2):
    return num1 + num2
sum = add(1,6)
print(sum)


# parameters are when you defining a function they are going to be the variables that you can use within the function.
#arguments exist at the time of calling the function.Arguments are values that you pass in for those parameters when you call the function.
def contact_card(name,age,car_model):
    return (f"{name} is {age} and drives  a {car_model}")

person_info = contact_card("Kevin",25,"Honda Civic")
print(person_info)

#if we know the parameter names and don't know what their order is. we can assign them known as keyword arguments
contact_card(age = 25,car_model='Honda Civic',name='kevin')

#mixing  positional and keyword  arguments
contact_card("kevin",car_model="Honda Civic",age=25)
#whenever you use keyword arguments you must continue using keyword arguments for the rest of function call.
#contact_card(age = 25, "kevin", car_model="Civic") 
#will get error for the above line of code as SyntaxError: positional argument follows keyword argument
# can use positional argument first and then use keyword arguments or you can use all positional or use all keyword 


#default argument value
def can_drive(age, driving_age = 16):
    return age >=  driving_age 
result = can_drive(29) # the secon parameter have the default value . so not needed to pass the value for it.
print(result)

can_drive(16,driving_age=18) #positional with keyword argumnet
can_drive(16,18) #positional arguments

# Note: SyntaxError: non-default argument follows default argument
# when we defining parameter if we ever have default argumnet for one of the parameters,then every parameter needs to also have default arguments
#def can_drive(age, driving_age = 16,vehicle_type):
#    pass