def AddToArray(num, k):
    make_number = 0
    for number in num:
        make_number = make_number * 10 + number
    make_number = make_number + k
    array_form = []
    while make_number != 0:
        extract_integer = make_number % 10
        array_form.append(extract_integer)
        make_number = make_number // 10
    return array_form[::-1]


if __name__ == "__main__":
    print(AddToArray([1, 2, 0, 0], 34))
