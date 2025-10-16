def FindIndices(nums, target):
    for i in range(len(nums)):
        min_ = i
        for j in range(i + 1, len(nums)):
            if nums[min_] > nums[j]:
                min_ = j
        nums[i], nums[min_] = nums[min_], nums[i]
    return nums
    left = 0
    l = []
    while left < len(nums):
        if nums[left] == target:
            l.append(left)
        left += 1
    return l


def FindIndicesOptimal(nums, target):
    nums.sort()
    left = 0
    l = []
    while left < len(nums):
        if nums[left] == target:
            l.append(left)
        left += 1
    return l


import time

# start = time.perf_counter()
# print(FindIndices([1, 2, 5, 2, 3], target=2))
# end = time.perf_counter()
# total_time = (end - start) * 1000
# print(total_time)
# start_ = time.perf_counter()
# print(FindIndicesOptimal([1, 2, 5, 2, 3], target=2))
# end_ = time.perf_counter()
# total_time_ = (end_ - start_) * 1000
# print(total_time_)
print(FindIndices(['9', '3', '6', '31', '2', '7', '5'], target=2))