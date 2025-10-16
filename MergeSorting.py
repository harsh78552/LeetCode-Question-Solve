def Sorting(array1, array2):
    sorted_array = []
    left_pointer = 0
    right_pointer = 0
    while left_pointer < len(array1) and right_pointer < len(array2):
        if array1[left_pointer] <= array2[right_pointer]:
            sorted_array.append(array1[left_pointer])
            left_pointer += 1
        else:
            sorted_array.append(array2[right_pointer])
            right_pointer += 1
    if left_pointer < len(array1):
        while left_pointer < len(array1):
            sorted_array.append(array1[left_pointer])
            left_pointer += 1
    if right_pointer < len(array2):
        while right_pointer < len(array2):
            sorted_array.append(array2[right_pointer])
            right_pointer += 1
    return sorted_array


def Merge(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    x = Merge(right_array)
    y = Merge(left_array)
    return Sorting(x, y)
print(Merge([2,1,4,3,5]))
