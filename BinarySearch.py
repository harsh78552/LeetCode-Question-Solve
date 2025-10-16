def search(nums, target):
    start = 0
    end = len(nums)
    mid = (start + end) // 2
    if target <= nums[mid]:
        while start <= mid:
            if nums[start] == target:
                return start
            start += 1
    else:
        while mid < end:
            if nums[mid] == target:
                return mid
            mid += 1
    return -1




print(search([-1, 0, 3, 4, 9, 12], 2))
