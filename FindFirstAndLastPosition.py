def searchRange(nums, target):
    index_first_last = [-1, -1]
    i = 0
    j = len(nums) - 1
    if not nums:
        return index_first_last
    elif len(nums) == 1:
        if nums[0] >= target != 0:
            index_first_last[0] = 0
            index_first_last[-1] = 0
        else:
            return index_first_last
    else:
        while i <= j:
            if nums[i] == target:
                index_first_last[0] = i
                break
            i += 1
        while j >= i:
            if nums[j] == target:
                index_first_last[-1] = j
                break
            j -= 1
    return index_first_last


# print(searchRange([5, 7, 7, 8, 8, 10], 8))
# print(searchRange([-1], 0))
# print(searchRange([5, 7, 7, 8, 8, 10], 6))
# print(searchRange([1], 1))
print(searchRange([1], 1))
# print(searchRange([1], 0))
# print(searchRange([1, 4], 4))
