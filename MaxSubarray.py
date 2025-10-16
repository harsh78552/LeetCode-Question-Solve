def maxSubarray(nums):
    current_sum = 0
    max_sum = nums[0]
    for num in nums:
        current_sum += num
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum


# print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubarray([-1]))
