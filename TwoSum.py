def TwoSum(nums, target):
    i = 0
    indices_frequency = {}
    for index, value in enumerate(nums):
        indices_frequency[value] = index
    for num in range(i + 1, len(nums)):
        search_number = target - nums[i]
        if search_number in nums[num:] and search_number + nums[i] == target:
            return [i, indices_frequency[search_number]]
        i += 1


if __name__ == "__main__":
    print(TwoSum([2, 7, 11, 15], 9))
    # print(TwoSum([3, 2, 4], 6))
    # print(TwoSum([3, 2, 3], 6))
