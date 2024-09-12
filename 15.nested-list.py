# Nested lists: Matrices and Cubes
# list can contain list

my_matrix = [[1,2,3],
             [4,5,6]]
print(my_matrix)
row_count = len(my_matrix) #2
print(row_count)
column_count = len(my_matrix[0]) 
print(column_count) # 3

# to get the  2nd column value in the first row 
second_item_first_raw =  my_matrix[0][1]
print(second_item_first_raw)


# to get the  3rd column value in the second row 
third_item_second_raw  = my_matrix[1][2]
print(third_item_second_raw)