def MoveZeros(nums):
    i = 0
    j = 1
    while i < j < len(nums):
        if nums[i] == nums[j]:
            nums[i + 1] = nums[j]
            i+=1
        j+=1
    return nums

print(MoveZeros([]))