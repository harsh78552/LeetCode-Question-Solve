def RemoveDuplicate(s):
    last_index = [0] * 26
    check_duplicate = [False] * 26
    for index, char in enumerate(s):
        x = ord(char) - ord("a")
        if last_index[index] == 0:
            last_index[x] = index
        else:
            last_index[x] = index
    stack = []
    for index, char in enumerate(s):
        if check_duplicate[ord(char) - ord('a')]:
            continue
        while stack and ord(stack[-1]) > ord(char) and last_index[ord(stack[-1]) - ord('a')] > index:
            x = stack.pop()
            check_duplicate[ord(x) - ord('a')] = False
        stack.append(char)
        check_duplicate[ord(char) - ord('a')] = True
    return "".join(stack)


print(RemoveDuplicate("bcabc"))
