def maxAscendingSum(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    for num in range(1, len(nums)):
        if nums[num - 1] < nums[num]:
            current_sum += nums[num]
            max_sum = max(max_sum, current_sum)
        else:
            current_sum = 0
            current_sum += nums[num]
            max_sum = max(max_sum, current_sum)
    return max_sum


# print(maxAscendingSum([10, 20, 30, 5, 10, 50]))
# print(maxAscendingSum([10, 20, 30, 40, 50]))
# print(maxAscendingSum([100, 10, 1]))