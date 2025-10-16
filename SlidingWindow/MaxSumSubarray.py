def MaxSumSubarray(array, size):
    sum_ = sum(array[:size])
    max_sum = sum_
    i = size
    j = 0
    while i < len(array):
        sum_ = (sum_ + array[i]) - array[j]
        max_sum = max(max_sum, sum_)
        i += 1
        j += 1
    return max_sum


if __name__ == "__main__":
    print(MaxSumSubarray([2, 5, 1, 8, 2, 9, 1], 2))
