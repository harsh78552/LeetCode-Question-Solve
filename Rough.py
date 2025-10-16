# matrix = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]
matrix = [[5, 8, 9], [10, 7, 6], [3, 1, 2]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j:
#             print(matrix[i][j], end=' ')
#         else:
#             print('*', end=' ')
#     print()
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if j >= i:
#             print(matrix[i][j], end=' ')
#         else:
#             print('*', end=' ')
#     print()
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i >= j:
#             print(matrix[i][j], end=' ')
#         else:
#             print('*', end=' ')
#     print()
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i + j == 2:
#             print(matrix[i][j], end=' ')
#         else:
#             print('*', end=' ')
#     print()
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix[i])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(matrix)
