def RemoveDuplicatesFromSort(nums):
    i = 0
    j = 1
    count_ = 0
    while i < j < len(nums):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
            count_ += 1
        j += 1
    return count_ + 1


if __name__ == "__main__":
    # print(RemoveDuplicatesFromSort([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(RemoveDuplicatesFromSort([1, 1, 2]))
