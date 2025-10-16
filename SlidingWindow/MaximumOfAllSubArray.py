def MaxSubarray(array, k):
    new_array = []
    for num in range(len(array) - k + 1):
        array_ = array[num:num + k]
        max_ = max(array_)
        new_array.append(max_)
    return new_array


if __name__ == "__main__":
    print(MaxSubarray([1, 3, -1, -3, 5, 3, 6, 7], 3))
