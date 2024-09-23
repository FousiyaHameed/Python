
# other easy way 
def is_palindrome(item):
    print(item)
    print(item[::-1])
    return item == item[::-1]
word = input("Enter a  word to check whether it is palindrome or not: ")
print(is_palindrome(word))
