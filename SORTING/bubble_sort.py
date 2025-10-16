def BubbleSort(array):
    for i in range(len(array) - 2, - 1, -1):
        is_swap = False
        for j in range(0, i + 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_swap = True
        if not is_swap:
            return
    return array


print(BubbleSort([5, 8, 1, 6, 9, 2, 4]))
