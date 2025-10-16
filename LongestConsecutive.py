def LongestConsecutive(nums):
    nums = set(nums)
    max_count = 0

    if not nums:
        return max_count
    else:
        for num in nums:
            if num - 1 not in nums:
                j = 1
                count = num
                while count + 1 in nums:
                    j += 1
                    count += 1
                max_count = max(max_count, j)

    return max_count


# print(LongestConsecutive([100, 4, 200, 1, 3, 2]))
print(LongestConsecutive([0, 7, 2, 5, 9, 8, 4, 6, 0, 1, 100, 101, 102, 103, 104, 105, 106, 107]))
# print(LongestConsecutive([1, 0, 1, 2]))
# print(LongestConsecutive([2, 3, 4, 1]))
# print(LongestConsecutive([1, 2, 100]))
