def sort(array):
    for i in range(len(array)):
        min_ = i
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                min_ = j
        array[i], array[min_] = array[min_], array[i]
    return array


def sortDutchAlgorithm(array):
    low = 0
    mid = 0
    high = len(array) - 1
    while mid <= high:
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    print(array)


print(sort([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
print(sortDutchAlgorithm([0, 1, 2, 0, 1, 2]))
