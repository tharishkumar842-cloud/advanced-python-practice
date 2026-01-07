matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened=[x for row in matrix for x in row if x >4]
print(flattened)