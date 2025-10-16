def CheckSortedArray(array):
    for j in range(len(array) - 2, -1, -1):
        is_swap = False
        for i in range(0, j + 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_swap = True
        if not is_swap:
            return True
        else:
            return False


print(CheckSortedArray([3, 5, 6, 8, 91, 10, 20]))
