import time


def findMin(nums):
    start = 0
    end = len(nums) - 1
    # min_val = float('inf')
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
        print(start,end,mid)
    return nums[start]

    #     min_val = min(min_val, min(nums[start], nums[end]))
    #     start += 1
    #     end -= 1
    # return min_val


start_ = time.perf_counter()
# print(findMin([3, 4, 5, 1, 2]))
# result = findMin([11, 13, 15, 17])
result = findMin([4, 5, 6, 7, 0, 1, 2])
end_ = time.perf_counter()
total_time = (end_ - start_) * 1000
print(result)
print(f"{total_time}")
