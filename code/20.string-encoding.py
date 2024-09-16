# in python3 the default encoding for a string is unicode, specifically UTF-8
# Unicode Transformation format()UTF
print(ord('a')) # code point for 'a' is 97
print(ord('™')) #8482 - to write Trademark (™) symbol press  alt+0153




# Another popular encoding type is ASCII can handle letters numbers and common punctuation.
# The extended ASCII format can hold 256 code points.The majority of those the first 128 and the first 128 code points for ASCII are valid in UTF 8

print(0x2122) # written in hexadecimal format and python gives always integer back 8482
print(ord('\u2122')) # 8482
print('\u2122')    # ™

# to get code point back to string
print(chr(8382)) # ₾
print(chr(8482)) # ™


#string methods
my_str = 'tEsTinG'
#converting string to lower case
print(my_str.lower()) #testing

#capitalize every letter
print(my_str.upper()) # TESTING

#capitalize the first letter and lowercase in the remaining letters
print(my_str.capitalize()) # Testing

my_str = 'This is a multiword string'
# capitalize the first letter of each unique word
print(my_str.title()) # This Is A Multiword String

email_id = 'Kevin@example.com'
print(email_id == 'kevin@example.com') #False
print(email_id.lower() == 'kevin@example.com') #True (all of the characters in here can be represented as an ASCII string)

my_str = 'testing'
print(my_str.isascii()) ##True (all of the characters in here can be represented as an ASCII string) 
print(my_str.islower())# True
print(my_str.isupper()) # False
print(my_str.istitle()) # False

# return a new string and then call another method onto
print(my_str.title().istitle()) #True

print(" ".isspace()) #True
print("f".isspace()) #False

print("'1.0' is decimal","1.0".isdecimal()) # False
print("'1' is decimal","1".isdecimal()) #True
print("'a' is decimal","a".isdecimal()) #False
print("'1' is digit","1".isdigit()) #True
print("'1.0' is numeric","1.0".isnumeric()) #False
print("'10' is numeric","10".isnumeric()) #True
print("'1a' is alpha","1a".isalpha()) #False
print("adgfdhh is alpha","adgfdhh".isalpha()) #True

print("'1bear' is identifier","1bear".isidentifier()) #False
print("'word' is identifier","word".isidentifier()) #True

print( "'This is printable' is printable","This is printable".isprintable()) #True

#return False even though we can print this. because it has an escape character. escape characters seen right here 
# cannot printed out because they just cause to do the screen to do something different in a sense.
print("This is printable\n".isprintable()) # False
print("This is printable\n")


# can work with as tokens, can have them be a collection of duifferent things
phrase = "This is a simple phrase"
words = phrase.split() # ['This', 'is', 'a', 'simple', 'phrase']
print(words)


url = "https://example.com/users/jimmy"
user = url.split('/') 
print(user) # ['https:', '', 'example.com', 'users', 'jimmy']
url_last_word = url.split('/')[-1] # jimmy
print(url_last_word)

#joiin
print(", ".join(words)) # This, is, a, simple, phrase
print(" ".join(words)) # This is a simple phrase

lines = ['First line', 'Second line', 'Third line']
output = '\n'.join(lines)
# inserted a new line character after each item so,the output would be in individual lines
print(output) # First line
              # Second line
              # Third line
# substitution grouping
template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"
my_str = template.format('Keith','Python')
#my_str = template.format('Keith')#IndexError: Replacement index 1 out of range for positional args tuple
#my_str = template.format('Keith','Python','true') # if we provided more value , it would disregard the value  instead of throwing an eror
print(my_str)

#Another way to use subtitute the same value in multiple different spots
template1 = "Hello, my name is {0}. and I really enjoy {1}. Have a nice day! - {0}"
print(template1.format('keith','python'))