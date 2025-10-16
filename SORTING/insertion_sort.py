def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        for k in range(i - 1, -1, -1):
            if array[k] > key:
                array[k + 1] = array[k]
            else:
                array[k + 1] = key
                break
        else:
            array[0] = key
    return array


print(InsertionSort([3, 5, 6, 4, 8, 9, 10, 7, 1]))
