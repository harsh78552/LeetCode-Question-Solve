def OptimalFindDuplicate(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            return abs(num)


# print(FindDuplicate([3, 1, 3, 4, 2]))
# print(OptimalFindDuplicate([3, 1, 3, 4, 2]))
print(OptimalFindDuplicate([1, 3, 4, 2, 2]))
# print(OptimalFindDuplicate([1, 1, 2]))
# print(OptimalFindDuplicate([1, 2, 2]))

