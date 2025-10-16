def maximumCount(nums):
    negative_count = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            negative_count += 1
        else:
            break
    positive_count = 0
    for j in range(negative_count, len(nums)):
        if nums[j] == 0:
            pass
        else:
            positive_count += 1
    return max(negative_count, positive_count) 


# print(maximumCount([-3, -2, -1, 0, 0, 1, 2]))
# print(maximumCount([5,20,66,1314]))
print(maximumCount([-2, -1, -1, 1, 2, 3]))
