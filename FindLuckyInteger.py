def findLuckyInteger(arr):
    new_dict = {}
    max_value = 0
    for num in arr:
        if num not in new_dict:
            new_dict[num] = 1
        else:
            new_dict[num] += 1
    for key, value in new_dict.items():
        if key == value:
            max_value = max(max_value, value)
    return max_value if max_value > 0 else -1


# print(findLuckyInteger([2, 2, 3, 4]))
# print(findLuckyInteger([1, 2, 2, 3, 3, 3]))
# print(findLuckyInteger([2, 2, 2, 3, 3]))
print(findLuckyInteger([2, 2, 3, 4]))
