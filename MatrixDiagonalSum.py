def MatrixDiagonalSum(mat):
    n = len(mat)
    total_sum = 0
    for i in range(len(mat)):
        if i == n - i - 1:
            total_sum += mat[i][i]
        else:
            total_sum += mat[i][i] + mat[i][n - i - 1]
    return total_sum


if __name__ == "__main__":
    print(MatrixDiagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
