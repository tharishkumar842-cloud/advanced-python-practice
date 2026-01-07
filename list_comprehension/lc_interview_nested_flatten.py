matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list=[x for rows in matrix for x in rows]
print(new_list)