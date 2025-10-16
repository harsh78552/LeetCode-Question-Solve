def TransposeMatrix(matrix):
    for index in range(len(matrix)):
        for index_ in range(index + 1, len(matrix)):
            matrix[index][index_], matrix[index_][index] = matrix[index_][index], matrix[index][index_]

    for j in range(len(matrix)):
        start = 0
        end = len(matrix[j]) - 1
        for _ in range(len(matrix[j]) // 2):
            if start <= end:
                matrix[j][start], matrix[j][end] = matrix[j][end], matrix[j][start]
            start += 1
            end -= 1
    return matrix






if __name__ == "__main__":
    # print(TransposeMatrix())
    # print(ReverseRowOfMatrix([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
    print(TransposeMatrix([[1,2,3],[4,5,6],[7,8,9]]))
