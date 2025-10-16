def ConsecutiveOnes(nums):
    frequency =0
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == 1:
            frequency += 1
        else:
            frequency = 0
        count = max(count, frequency)
        i += 1
    return count


print(ConsecutiveOnes([1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]))
print(ConsecutiveOnes([1, 0, 1, 1, 1, 1, 0, 1]))
print(ConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(ConsecutiveOnes([1, 1, 0, 1]))
print(ConsecutiveOnes([1, 0, 1, 0]))
