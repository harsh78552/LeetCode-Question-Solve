def RemoveDuplicate(array):
    i = 0
    while i < len(array):
        if array[i] == 0:
            break
        i += 1
    if i == len(array):
        return
    j = i + 1
    while j < len(array):
        if array[j] != 0:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    return array


print(RemoveDuplicate([0, 1, 0, 3, 12]))
