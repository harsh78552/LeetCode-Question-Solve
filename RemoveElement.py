def RemoveElement(nums, vals):
    for number in nums[:]:
        if number == vals:
            nums.remove(vals)
    return nums


if __name__ == '__main__':
    print(RemoveElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
