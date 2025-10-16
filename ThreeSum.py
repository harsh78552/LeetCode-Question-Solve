def ThreeSum(nums):
    store_number = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum_ = nums[i] + nums[j] + nums[k]
            if sum_ < 0:
                j += 1
            elif sum_ > 0:
                k -= 1
            else:
                if sum_ == 0:
                    store_number.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
    return store_number


if __name__ == "__main__":
    print(ThreeSum([-1, 0, 1, 2, -1, -4]))
