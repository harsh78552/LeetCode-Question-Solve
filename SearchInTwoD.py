def searchMatrix(matrix, target):
    array_found = 0

    for j in range(len(matrix)):
        if matrix[j] == 1 and target == matrix[j][0]:
            array_found = matrix[j]
        else:
            if matrix[j][0] <= target <= matrix[j][-1]:
                array_found = matrix[j]

    start_index = 0
    if not array_found:
        return False
    end_index = len(array_found) - 1
    if len(array_found) == 1:
        if array_found[0] == target:
            return True
    else:
        while start_index <= end_index:
            mid = len(array_found) // 2
            if array_found[mid] >= target:
                if array_found[start_index] == target:
                    return True
                start_index += 1
                end_index = mid
            else:
                if array_found[end_index] == target:
                    return True
                start_index = mid
                end_index -= 1
    return False


if __name__ == "__main__":
    # print(searchMatrix([[1, 3, 5, 7, 8], [10, 11, 16, 20], [23, 30, 34, 60]], 7))
    # print(searchMatrix([[1]], 1))
    print(searchMatrix([[1], [3]], 3))
