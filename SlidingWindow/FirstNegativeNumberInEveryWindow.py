def FirstNegative(array, size):
    result = []
    for num in range(len(array) - size + 1):
        window = array[num:num + size]
        first_negative_number = 0
        for num_ in window:
            if num_ < 0:
                first_negative_number = num_
                break
        if first_negative_number < 0:
            result.append(first_negative_number)
    return result


if __name__ == "__main__":
    print(FirstNegative([12, -1, -7, 8, -15, 30, 16, 28], 3))
