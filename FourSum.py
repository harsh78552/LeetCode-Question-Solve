def ThreeSum(nums, target=None):
    nums.sort()
    store_list = []
    for index in range(len(nums)):
        if index > 0 and nums[index] == nums[index - 1]:
            continue
        for j in range(index + 1, len(nums)):
            if j > index + 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            m = len(nums) - 1
            while l < m:
                checkSum = nums[index] + nums[j] + nums[l] + nums[m]
                if checkSum < target:
                    l += 1
                elif checkSum > target:
                    m -= 1
                else:
                    if checkSum == target:
                        store_list.append([nums[index], nums[j], nums[l], nums[m]])
                        l += 1
                        m -= 1
                        while l < m and nums[l] == nums[l - 1]:
                            l += 1
                        while l < m and nums[m] == nums[m + 1]:
                            m -= 1
    return store_list


if __name__ == "__main__":
    print(ThreeSum([1, 0, -1, 0, -2, 2], 0))
    # print(ThreeSum([2, 2, 2, 2, 2], 8))
    # print(ThreeSum([-1, 0, 1, 2, -1, -4]))
