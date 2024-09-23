# Generators are Python functions that behave like iterator.kind of range function.
# reimplement range function using a generator
def gen_range(stop,start=1,step = 1):
    num = start
    while num <= stop:
        yield num # yeild works like return and once it returns the first time it's going to stop, so it's not 
        #continue on with loop. it's going to stop right here until we ask it for the next item and then  going
        # to pick up where it left off and continue on until it yeilds again.
        num += step

# in terminal , we can load this into the interpreter using the 'i' flag 
# python -1 gen.py
#normally we call a function,it's going to execute itself like the body of the function and return something. 
# but since this a generator function, it's going to return a generator object.

#>>> gen_range(5)             
#<generator object gen_range at 0x0000029CBE74B920>

# To get actual value from it, need to use 'next' built in function
#>>> generator = gen_range(5)  
#>>> next(generator)
#1
#>>> next(generator)
#2
#>>> next(generator)
#3
#>>> next(generator)
#4
#>>> next(generator)
#5
#>>> next(generator)
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#StopIteration
#>>>  # thrown a stopiteration error.beacuse we reach very end of generator function body.  
      # completed the loop and so,condition (num <= stop) returned false.



#in practice , the way that we are  going to use this would be something like
for num in gen_range(10, step =2):
    print(num)  # result will be 1,3,5,7,9


# we won't manually be calling the function the next function very often with genrators. we will be using them inthe context of for loops


# Converting generators to lists
#>>> generator = gen_range(10)
#>>> list(generator)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#infinite loop
def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
  

       
#exit and realod python file
#fib = gen_fib()
#next(fib)
#list(fib)  ### this will cause to loop infinte  number of times, never ends 

#sice the loop dosn't have a break statement. if we try to do list(fib) it,s going to go forever,it's never going to return 
#  to us because it's continue calculating things untill it eventually gets killed by the fact that it's gone on too long. 
# this will be the potential issue trying to turn generators into lists


# to know how fast a generator version of  the fibonacci sequence can be. we can create a giant list using fibonacci quiquly 
# as long as we restrict how many times we want to do it

# execute in terminal(python -i gen.py)
 #>>> def gen_fib():
#...     a, b = 0, 1
#...     while True:
#...         a, b = b, a + b
#...         yield a
#... 
#>>> fib= gen_fib()
#>>> [next(fib) for _ in range(50)][-1]   #calculate the 50th number (50th number in the fibonacci sequence is 12586269025)
#12586269025

# Note: in recursion we couldn't actually calculate the 50th number in the fibonacci sequence, 
# because it is taking too long with recursion but you could do it pretty quick and easily using a generator