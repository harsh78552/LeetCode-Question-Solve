def MisingNumber(nums):
    nums.sort()
    j = 0
    for i in range(len(nums)):
        if j < len(nums) and nums[j] != i:
            return i
        j += 1
    return j


print(MisingNumber([0, 1]))
print(MisingNumber([3, 0, 1]))
