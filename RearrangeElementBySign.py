def RearrangeElement(nums):
    positive_list = []
    negative_list = []
    for num in nums:
        if num > 0:
            positive_list.append(num)
        else:
            negative_list.append(num)

    merged_list = []
    for index in range(len(positive_list)):
        merged_list.append(positive_list[index])
        merged_list.append(negative_list[index])
    return merged_list


print(RearrangeElement([3, 1, -2, -5, 2, -4]))
