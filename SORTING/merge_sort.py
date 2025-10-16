def Sorting(array1, array2):
    sorted_array = []
    left = 0
    right = 0
    while left < len(array1) and right < len(array2):
        if array1[left] < array2[right]:
            sorted_array.append(array1[left])
            left += 1
        else:
            sorted_array.append(array2[right])
            right += 1

    if left < len(array1):
        while left < len(array1):
            sorted_array.append(array1[left])
            left += 1

    if right < len(array2):
        while right < len(array2):
            sorted_array.append(array2[right])
            right += 1
    return sorted_array


def Merge(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    array_ = Merge(left_array)
    array__ = Merge(right_array)
    return Sorting(array_, array__)


print(Merge([5, 8, 1, 6, 9, 2, 4]))
