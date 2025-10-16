from functools import cmp_to_key


def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


def largestNumber(nums):
    nums_string = []
    for num in nums:
        nums_string.append(str(num))
    lexical_sorting = sorted(nums_string, key=cmp_to_key(compare))
    if lexical_sorting[0] == '0':
        return '0'
    else:
        return "".join(lexical_sorting)


# print(largestNumber([3, 30, 34, 5, 9]))
print(largestNumber([9, 3, 6, 30, 2, 7, 5]))
