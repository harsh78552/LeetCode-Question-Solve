def plusOne(digits):
    extract_digit = 0
    for num in digits:
        extract_digit = extract_digit * 10 + num
    extract_digit = extract_digit + 1
    new_array = []
    for digit in str(extract_digit):
        new_array.append(int(digit))
    return new_array


print(plusOne([4, 3, 2, 1]))
