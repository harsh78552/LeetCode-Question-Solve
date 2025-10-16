def ReverseArray(x, y, array):
    mid = len(array) // 2
    if x >= y:
        print(array)
        return
    array[x], array[y] = array[y], array[x]
    ReverseArray(x + 1, y - 1, array)


ReverseArray(0, 7, [5, 7, 3, 2, 6, 1, 5, 9])


def WhileReverseArray(array):
    left = 0
    right = len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array
print(WhileReverseArray([5, 7, 3, 2, 6, 1, 5, 9]))