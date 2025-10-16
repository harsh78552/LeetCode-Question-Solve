def CharacterFrequency(string, array):
    frequency_list = [0] * 26
    for char in string:
        index = ord(char) - ord('a')
        frequency_list[index] += 1
    for char in array:
        index = ord(char) - ord('a')
        print(frequency_list[index])


print(CharacterFrequency('azyvyyzaaaa', ['d', 'a', 'y', 'v']))
