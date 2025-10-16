def SecondLargest(array):
    array_ = []
    largest_element = max(array)
    num = largest_element - array[0]
    second_largest = 0
    for index in range(1, len(array)):
        if largest_element - array[index] < num:
            second_largest = array[index]
        num = largest_element - array[index]
    array_.append(second_largest)

    smallest_element = min(array)
    smallest_num = abs(largest_element - array[0])
    second_smallest = 0
    for index in range(1, len(array)):
        if smallest_element - array[index] > smallest_num:
            second_smallest = array[index]
        smallest_num = smallest_element - array[index]
    array_.append(second_smallest)
    return array_


print(SecondLargest([55, 32, 97, -55, 45, 32, 88, 21]))
