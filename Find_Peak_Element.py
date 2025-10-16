def findPeakElement(nums):
    start = 1
    end = len(nums) - 1
    mid = (start + end) // 2
    if len(nums) <= 1:
        return 0
    else:
        while start < mid:
            if nums[start - 1] < nums[start] and nums[start + 1] < nums[start]:
                return start
            start += 1
        while end >= mid:
            if nums[end - 1] < nums[end]:
                if end - mid != 1:
                    return end
                else:
                    return end
            end -= 1
    return 0


print(findPeakElement([1, 1, 1, 2, 2, 6, 4]))
print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([2,1]))
print(findPeakElement([1, 2, 3]))
