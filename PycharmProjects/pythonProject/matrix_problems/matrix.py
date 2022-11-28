def increment_one(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y]==1:
                matrix[x][y] = 2
    return matrix

print(increment_one([[1,0,1],[1,1,0],[0,0,1]]))
