# Python

Entry level python programe.

The Certified Entry-Level Python Programmer Certification (PCEP) is a great place to start when getting Python certified. This course is designed to learn the fundamentals of Python required to take and pass the Certified Entry-Level Python Programmer Certification exam before moving onto the more advanced certifications.

Throughout this course, we'll cover:

Python data types
Control flow structures — conditionals and loops
Data collections
Functions and generators


#number systems
**There is more than one way to represent a number**

Decimal: 15    Binary:1111

Number systems are specified their base number.

Decimal is base 10

Binary is base 2

**Common  Number Systems**
Decimal - Base 10 (0 - 9)

Binary - Base 2 (0 - 1)

Octal - Base 8 (0 - 7)

Hexadecimal - Base 16 (0-F( 0-9 + A -F))

**Representing Number systems in Python**
Binary Prifix 0b 0b1001

Octal Prifix 0o 0o7242

Hexadecimal Prifix 0x 0xFF012


# Converting the decimal number 15 to Binary
 15/2 => 7 with remainder of 1  ---least significant

 7/2 => 3 with remainder of 1

 3/2 => 1 with remainder of 1

 1/2 => 0 with remainder of 1  # -- most significant

     once we get zero we know we reached end of conversion.

Binary Number: 1111 

**Converting  back from  binary to decimal**
 Binary Number: 1111

(1*2**3) + (1*2**2) + (1*2**1) + (1*2**0)  

 8 + 4 + 2 + 1  =  15

# Floating-Point-Accuracy
 Floating-point numbers are stored as binary  fractions in memeory.

 Not all decimals can be represented as binary fractions.

 Examples: 0.1 can't be represented cleanly

 It approxiates to something like: 0.

 1000000000000000055511151231257827021181583404541015625

 Not all floats are perfectly accurate to what we want them to be written as decimal notation because of how the computers work and this means  that in certain circumferences, which are not super common, but when you run into these issues,they are actually kind of hard to track down. You can run into odd rounding issues that are super far down the line. So, if you are in a situation where you are working with that level of pricision, then you might want to consider finding a different way to do your math and this is you will run  into things sometimes and oftentimes if you are working with something like money just don't use floats at all, just convert things into cents, for instance, and then always work with integers. So that's one way to kind of get around this particular thing. because integers can always be cleanly converted from one type to another.

 # Unary and Biwise Operators
 Unary operator, that's going to be an operator that only has one operation.
 1 + 1

plus has 2 operands ,left and right, but unary opertor is going have only one .

example:

~1 # bitwise complement operator.
all of the bitwise operators work on the binary components that we have.
we are going to work with integers . we are  going to create a variable 'a' and make it as binary integer,0b010 this going to be 2 actually.

a = 0b010

a

2

bin(a)

'0b10'


the bitwise complement operator here this tilde(~) operator little bit wired because you  don't have too many situations where you are really going to need to use it but what it does is it convers over to what's known as the 2's complement of binary representation. 2's complement means that we have a way to represent kind of negative number and it always starts with one.

~a

-3

bin(~a) 

'-0b11'

have formula to know what exactly the operator does,-1 * a - 1

a value was 2 (0b010)

-1 * 2 - 1

-2 - 1 = -3 which is -0b11


**AND OR XOR NOT**
1 consider as true and 0 consider as false
**OR** -  require either of the values is true and return true value
a = 0b1001

b = 0b1100

bin(a|b)

'0b1101'

1 1 = true  1

0 1 = true  1

0 0 = false 0

1 0 = true  1, so will get 0b1101

**AND** - require both value should be true otherwise return false.
a = 0b1001 

b = 0b1100

bin(a & b) 

'0b1000'

1 1 true  - both values is true so return 1.

0 1 false - one value is true so return false 0.

0 0 false  - both values is false so return false 0.

1 0 true  - one value is true so return false 0.

**XOR (Exclusive OR)** - require only one value should be true while comparing both value otherwise return false.

a = 0b1001 

b = 0b1100 

bin(a ^ b)

'0b101'

we expect the result as 0b0101 , but it will move the trailing zero.
so the result would be 0b101.

# shift operator (right shift bitwise operator >>, << left shift bitwise operator)

it will change the binary representation by moving the value to right or left.
example: for right shift bitwise operator(>>)

a = 0b110

bin(a >> 2)

'0b1'  

moving 2 value from the right (10), then will get result as 0b1


a = 0b110

bin(a >> 4)

'0b0'

moving 4 value from the right (0110), then will get result as 0b0

# example: for left shift bitwise operator (<<)
a = 0b110   

bin(a << 2) 

'0b11000'

adding 2 values to the end of the binary value.

a << 2

24

'0b11000'is result of bin(a << 2) and it's value is 24


a

6

'0b110'is ''a' and it's value is 6

we can do many of these ,it will just make the number  bigger and bigger.

bin(a << 4) 

'0b1100000'

a << 4      
96

'0b1100000'the binary result is equal to 96

# Boolean Operators
**NOT**
not True

False

not False

True

**or - either is true , the result is true**
True or True

True

True or False

True

False or False

False

False or True

True

**and - both  must be true to be true**
True and True    

True

True and False

False

False and False 

False

False and True

False

# Comparison Operators

1 < 1

False

2 > 1

True

2 < 1

False

1 <= 1

True

2.0 >= 3 

False

2.0 >= 2 

True


we don't strictly have to compare against numbers, we can compare other types;

'a' > 'b'

False

'b' > 'a'

True

'bb' >= 'ba'

True

It's really comparing each digit one at a time. so in the case of bb and ba.it's going to compare first value from the both side of the operator b and b are exactly same can't make comparison here and then b and a, we know  b is greater than a. so returns True.

'a' <= 'c'

True

you can see the numerical representation of kind of what it's doing behind the scenes for each of these charaters by doing the order function.

ord('a')

97

ord('A') 

65

capital A is distictly different than a lower case a

'A' <= 'a' 
True

'A' == 'a' 
False

'a' <= 1 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<=' not supported between instances of 'str' and 'int'

we get type error for this. you can't compare string and integer using this comparison operation.

the othe comparison operator that deal with whether or not the things are equal or equivalent to one another we use 2 eual sign == . Single equal sign we use for assignment operation.

1 == 1

True

1.0 == 1

True

2 == 1.0

False

'a' == 2 

False

'a' == 'a' 

True

if we ever want to determine something is not equal then we have an operator that too exclamation with equal sign (!=)

1 != 1

False

2 != 1.0

True

**is (identity operator)**
1 is 1

True

1 is 1 return True means is it has to be the exact same object. Basically take up the exactsame spot in memory. integers are immutable. every time we type in the  integer literal one , it's going to look the same spot of the memory because you can't modify an integer. so there is no reason for it to allocate a different spot on your computer to store it. once you have initialized it because there is no risk in it changing.

 1 is 1.0

False

because these are two distinct objects and they take 2 differnt spots in memory on your computer.

String are also immutable

'a' is 'a'

True

true becasue these take up the exact same spot in memory, because you can't change a string

**is not (opposite of the identity operator kind of compound operator)** 
'a' is not 'a' 

False


 we can checkout the id or basically that place in memory where these thing are going to stored and that's using the id function.

id('a')

140705874381648

it always reurn the same number.

id('a')

140705874381648

id('a')

140705874381648

id('a')

140705874381648

id('a')

140705874381648

it won't be the same number for you every time   you boot up apython process. it's going to look in the memory and it's going to allocate some stuff and put the value there and it's always look back to the same spot. next time you boot up you will know, the memory is going to be cleared in a different way and it's  going to have store things in a different spot on the actual hardware. but it will at least know  to point to  the exact same spot.

'a' is 'a' 

True

id('a') == id ('a')

True

[] is []

False 

false because you can modify an empty list. look exactly same , but we  could take  them seperately and make changes to them and they would definitely not the exact same  thing anymore. python will actually put these in different spots in memory to make sure there is no sort of clashing of things. 

# Operator Priority(Binding)

**Example:1**

14 & 3 * 2 + 4

10

calculated as  3 * 2  will take first which is 6 and then addition  + 4 , 6 + 4 = 10,
 will get 14 & 10.

14 & 10

10

to know how you get the result  10 while doing and(&) operation;

 14 in binary form 1110 

 10 in binary form 1010

                  --------

                   1010   which is 10

a = 1110

b = 1010 

bin(a & b)= 0b1010 


**Example:2**

14 & 3 * (2 + 4) 

2

calculated as;

14 & 3 * (2 + 4)

14 & 3 * 6

14 & 18  = 2

**Example:3**

(14 & 3) * 2 + 4 

8

calculated first 14 & 3 which is 2, then multiplication 2 * 2 = 4 then addition 4 +4 = 8

(14 & 3) * 2 + 4 

  2 * 2 + 4

  4 + 4 = 8

so the result is 8

**Example:4**

14 & (3 * 2) + 4 

10

calculated as;

14 & (3 * 2) + 4  

 14 & 6 + 4

 14 & 10 = 10

 so the result is 10.
 