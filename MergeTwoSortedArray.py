def MergedTwoSortedArray(a, b):
    merged_array = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if len(merged_array) == 0 or merged_array[-1] != a[i]:
                merged_array.append(a[i])
            i += 1
        else:
            if len(merged_array) == 0 or merged_array[-1] != b[j]:
                merged_array.append(b[j])
            j += 1

    while i < len(a):
        if len(merged_array) == 0 or merged_array[-1] != a[i]:
            merged_array.append(a[i])
        i += 1

    while j < len(b):
        if len(merged_array) == 0 or merged_array[-1] != b[j]:
            merged_array.append(b[j])
        j += 1

    return merged_array


print(MergedTwoSortedArray([1, 2, 3, 6, 7], [1, 2, 3, 4, 5]))
print(MergedTwoSortedArray([2, 2, 4, 6, 6, 8], [4, 4, 6, 7]))
