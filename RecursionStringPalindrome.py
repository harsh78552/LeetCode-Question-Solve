def LoopStringPalindrome(string):
    new_string = ''
    for char in string:
        new_string = char + new_string
    if new_string == string:
        return True
    else:
        return False


print(LoopStringPalindrome('nitin'))


def RecursionStringPalindrome(string, store_string='', num=0):
    if num >= len(string):
        if store_string == string:
            print(True)
        else:
            print(False)
        return
    RecursionStringPalindrome(string, string[num] + store_string, num + 1)


RecursionStringPalindrome('nitin')
