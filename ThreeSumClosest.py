def ThreeSumClosest(nums, target):
    nums.sort()
    nearest_sum = float('inf')

    for index in range(len(nums)):
        j = index + 1
        k = len(nums) - 1
        while j < k:
            currentSum = nums[index] + nums[j] + nums[k]
            if abs(currentSum-target) < abs(target - nearest_sum):
                nearest_sum = currentSum
            if currentSum < target:
                j += 1
            elif currentSum > target:
                k -= 1
            else:
                return currentSum
    return nearest_sum


if __name__ == "__main__":
    # print(ThreeSumClosest([-1, 2, 1, -4], 1))
    # print(ThreeSumClosest([0, 0, 0], 0))
    # print(ThreeSumClosest([0, 1, 2],0 ))
    print(ThreeSumClosest([-2,-1,1,4],0 ))
    # print(ThreeSumClosest([10, 20, 30, 40, 50, 60, 70, 80, 90], 1))
