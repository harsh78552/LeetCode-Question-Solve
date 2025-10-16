def FindPivot(nums):
    right_sum = 0
    for num in nums:
        right_sum += num
    left_sum = 0
    for num in range(len(nums)):
        right_sum -= nums[num]
        if right_sum == left_sum:
            return num
        left_sum += nums[num]
    return -1


# print(FindPivot([1, 7, 3, 6, 5, 6]))
print(FindPivot([1, 2, 3]))
