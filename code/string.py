# Strings and String Operators

# can be use single or double quote.in both ways ,it will not show the single or double quote in the printed result.
# always produce the single quoted string result string in REPL in both ways.
#  it's handy if we need to use the other type of quote inside whatever the textual information is.
print('single quoted string')
print("double quoted string")
# starts with a double and ends with single will give an error
# if string starts with single quote then end it with sindle quote
# if string starts with double quote then end it with double quote

print('''
      This is a triple quoted  
      multi-line string 
      ''')

print("pass"+"word")
print("Ha"*4)
#string is known as an object and python is object oriented language

my_char_position = "my test string"
print(my_char_position.find('t')) # index start with zero.

string_to_lower = "TesTiNG".lower()
print(string_to_lower)
print("Password123".lower())# it doesn't  do anything with 123 but doesn't give us error. will convert the P into lower case.

#escape sequences using back slash character
print("tab\tDelimited")# will give you some specific spacing when it is printed out "tab     Delimited"
print("New\nLine")

print("'single' in double") # 'single' in double
print('"double" in single') # "double" in single

print("\"Double\" in double") # "double" in double