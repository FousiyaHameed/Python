#Create the string-info.py Script and Take User Input
#Print the First, Last, and Middle Characters from the User's Input
#Print the Even Index Characters and Odd Index Characters
#Print the String in Reverse

#Expected result is as below:
#Enter a message: Test Message
#First character: T
#Last character: e
#Middle character: e
#Even index characters: Ts esg
#Odd index characters: etMsae
#Reversed message: egasseM tseT

message = input("Enter a mesage: ") 
print("First character:",message[0])
print("Last character:",message[-1])
print("middle character:",message[int(len(message)/2)])
print("Even index characters:",message[::2]) # it is similar to [0::2]
print("Odd index characters:",message[1::2])
print("string in reverse",message[::-1])





