def LogicSlicing(nums, k):
    if k > len(nums):
        k = k % len(nums)
    right = -1
    left = -k
    while right > left:
        nums[right], nums[left] = nums[left], nums[right]
        left += 1
        right -= 1

    left_ = 0
    right_ = len(nums) - k - 1
    index = len(nums) - k
    for i in range(index // 2):
        if left_ < right_:
            nums[left_], nums[right_] = nums[right_], nums[left_]
        left_ += 1
        right_ -= 1


    left__ = 0
    right__ = len(nums) - 1
    for _ in range(len(nums) // 2):
        if left__ < right__:
            nums[left__], nums[right__] = nums[right__], nums[left__]
        left__ += 1
        right__ -= 1
    return nums



print(LogicSlicing([1, 2, 3, 4, 5, 6, 7], 3))
