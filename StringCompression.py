def StringCompression(chars):
    count = 1
    write = 0
    for index in range(1, len(chars) + 1):
        if index < len(chars) and chars[index] == chars[index - 1]:
            count += 1
        else:
            chars[write] = chars[index - 1]
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            count = 1
    return write


# print(StringCompression(["a", "a", "b", "b", "c", "c", "c", 'a']))
print(StringCompression(["a", "a", "b", "b", "c", "c", "c"]))

