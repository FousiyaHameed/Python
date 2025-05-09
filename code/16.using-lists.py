# 1.Create a users List and Add Initial Items
# 2.Remove bob and Create rev_users List
# 3.Insert melody to users and Concatenate Lists
# 4.Slice`users to Return 3rd and 4th Elements


# From within the using-lists.py file, we'll be modifying the users list so that the assertions throughout
# the file all succeed eventually. As we're working through the tasks, we can run the file. 
# Whenever Python gets to a line that starts with assert,it will raise an error and stop executing 
# if we haven't met the criteria.
#This process will show us the line where the the script encountered an issue,
#  and show us the differences between our expected and actual values.


 # 1) Set the users variable to be an empty list

users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"
# 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.
users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

# 3) Remove 'bob' from the `users` list without reassigning the variable.
del users[1]

assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

# 4) Reverse the users list and assign the result to `rev_users`
rev_users = list(reversed(users))

assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"


# 5) Add the user 'melody' to users where 'bob' used to be.
users.insert(1, 'melody')
print('iserted to users',users)

assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

# 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command
users += ['andy', 'wanda', 'jim']
print(users)

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"
# 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
center_users = users[2:4]

assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"
