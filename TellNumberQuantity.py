def FindFrequency(array1, array2):
    frequency_dict = {}
    for num in array1:
        if num not in frequency_dict:
            frequency_dict[num] = 1
        else:
            frequency_dict[num] += 1

    for num in array2:
        if num not in list(frequency_dict.keys()):
            print(f"{num} = {0}")
        else:
            print(f"{num} = {frequency_dict[num]}")


FindFrequency([5, 3, 2, 2, 1, 5, 5, 7, 5, 10], [10, 11, 1, 9, 5, 67, 2])
