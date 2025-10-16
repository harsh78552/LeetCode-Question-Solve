def SetMatrixZero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(len(matrix[i])):
                    if matrix[i][k] == 0:
                        continue
                    else:
                        matrix[i][k] = '0'
                for m in range(len(matrix)):
                    if matrix[m][j] == 0:
                        continue
                    else:
                        matrix[m][j] = '0'
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if matrix[i][k] == '0':
                matrix[i][k] = 0
    return matrix


# print(SetMatrixZero([[7, 9, 2, 3], [20, 8, 0, 10], [29, 0, -10, 5], [4, 14, 6, 7]]))
# print(SetMatrixZero([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# print(SetMatrixZero([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(SetMatrixZero([[0],[1]]))
