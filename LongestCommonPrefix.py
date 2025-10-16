def LongestCommonPrefix(strs):
    sorted_strs = sorted(strs, key=len)
    stack = []
    for char in sorted_strs[0]:
        stack.append(char)
    for j in range(1, len(sorted_strs)):
        for k in range(len(sorted_strs[j])):
            if k < len(stack) and sorted_strs[j][k] != stack[k]:
                stack[k] = '0'

    str_ = ''
    for char in stack:
        if char.isdigit() is False:
            str_ += char
        else:
            break
    return str_


if __name__ == "__main__":
    print(LongestCommonPrefix(["flower", "flow", "flight"]))
    # print(LongestCommonPrefix(["cir","car"]))
