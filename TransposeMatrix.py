def TransposeMatrix(matrix):
    for j in range(len(matrix)):
        for k in range(j+1,len(matrix)):
           matrix[j][k],matrix[k][j]=matrix[k][j],matrix[j][k]
    return matrix


if __name__ == "__main__":
    print(TransposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(TransposeMatrix([[1, 2, 3], [4, 5, 6]]))
