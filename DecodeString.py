def DecodeString(s):
    while '[' in s:
        close = 0
        x = ''
        for index in range(len(s) - 1, -1, -1):
            if s[index] == ']':
                close = index
            else:
                if s[index] == '[':
                    open = index
                    digits = ""
                    for i in range(open + 1, close):
                        x += s[i]
                    j = index - 1
                    while j >= 0 and s[j].isdigit():
                        digits = s[j] + digits
                        j -= 1
                    y = int(digits) * x
                    s = s[:open + 1] + y + s[close + 1:]
                    break
    return s


# print(DecodeString('2[ab3[cd2[ef]]]'))
# print(DecodeString("2[abc]3[cd]ef"))
print(DecodeString('3[a100[c]]'))
# print(DecodeString('3[a]2[bc]'))
# print(DecodeString('100[leetcode]'))
