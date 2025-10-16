def dominantIndex(nums):
    max_num = max(nums)
    max_num_index = 0
    check = True
    i = 0
    while i < len(nums):
        if nums[i] == max_num:
            max_num_index = i
            i += 1
        else:
            if nums[i] + nums[i] > max_num:
                check = False
                break
            i += 1
    if check:
        return max_num_index
    else:
        return -1


inputList = [3, 6, 1, 0]
print(dominantIndex(inputList))
