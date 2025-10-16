def ReverseWordString(s):
    s = s.strip().split(" ")
    new_list = []
    for word in s[:]:
        if word != '':
            new_list.append(word)
    return " ".join(new_list[::-1])


print(ReverseWordString("the sky is blue"))

# print(ReverseWordString("a good   example"))
