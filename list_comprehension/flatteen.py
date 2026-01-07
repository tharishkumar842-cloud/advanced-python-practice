matrix = [[1,2],[3,4],[5,6]]
new_list=[x for rows in matrix for x in rows if x%2==0]
print(new_list)
