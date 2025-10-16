def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False


# print(increasingTriplet([1, 2, 3, 4, 5]))
# print(increasingTriplet([5, 4, 3, 2, 1]))
# print(increasingTriplet([2, 1, 5, 0, 4, 6]))
# print(increasingTriplet([20, 100, 10, 12, 5, 13]))
# print(increasingTriplet([2,4,-2,-3]))
# print(increasingTriplet([1, 2, 1, 3]))
# print(increasingTriplet([5, 1, 6]))
# print(increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
# print(increasingTriplet([2,4,-2,-3]))
print(increasingTriplet([10, 20, 30, 5, 10, 50]))
