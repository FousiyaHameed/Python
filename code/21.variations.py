#Print the Lowercase, Uppercase, Title Case, and Capitalized Versions of the User's Input

#Now that we have the message variable, we're going to print a few different things to the screen:

#The lowercase version using str.lower
#The uppercase version using str.upper
#The title case version using str.title
#The capitalized version using str.capitalize
#Let's use each of these methods combined with the print function:

message = input("Enter a message:  ")
print("Lowercase:",message.lower())
print("Uppercase:",message.upper())
print("Capitalized:",message.capitalize())
print("Title case:",message.title())


#Separate the String and Present the Individual Words as a List

#For the remaining requirements of our script, we need to work with the individual words. 
# Because of this, we're going to store the words off as a new variable, words. We can get the words by using the str.split method. 
# After we've separated the message into words, let's also print them out:
words = message.split( )
print("Words:",words)

#Print the Alphabetic First and Last Words from the User's Input
# We're going to sort the words in the words list alphabetically and save the new list to sorted_words by 
# using the sorted built-in function. Lastly, we'll print the alphabetic first and last words. Let's do this by indexing to 0 and -1.
sorted_words = sorted(words)
print("sorted: ",sorted_words)
print("Alphabetic first word:",sorted_words[0])
print("Alphabetic last word:",sorted_words[-1])


# Here's the final script running:

#Enter a message: This is a test message!
#Lowercase: this is a test message!
#Uppercase: THIS IS A TEST MESSAGE!
#Capitalized: This is a test message!
#Title Case: This Is A Test Message!
#Words: ['This', 'is', 'a','test','message!']
#Alphabetic First Word: This
#Alphabetic Last Word: test
