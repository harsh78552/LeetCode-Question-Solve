def search(nums, target):
    start = 0
    end = len(nums) - 1
    mid = (start + end) // 2
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    elif nums[mid + 1] > nums[mid] > nums[mid - 1]:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    else:
        if target >= nums[start] and mid != start:
            if target <= nums[mid]:
                while start <= mid:
                    if nums[start] == target:
                        return start
                    start += 1
            else:
                while start <= mid:
                    if nums[start] == target:
                        return start
                    start += 1
        else:
            while end >= mid:
                if nums[end] == target:
                    return end
                end -= 1
    return -1


# print(search([0, 1, 2, 4, 5, 6, 7], 6))
# print(search([1, 3], 3))
print(search([1], 0))
# print(search([5, 1, 3], 5))
# print(search([1, 3, 5], 5))
