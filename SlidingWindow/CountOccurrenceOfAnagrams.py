def CountOccurrence(array, word):
    word_frequency = {}
    count = 0
    for char in word:
        if char not in word_frequency:
            word_frequency[char] = 1
        else:
            word_frequency[char] += 1
    for num in range(len(array) - len(word) + 1):
        window = array[num:num + len(word)]
        window_char_frequency = {}
        for char in window:
            if char not in window_char_frequency:
                window_char_frequency[char] = 1
            else:
                window_char_frequency[char] += 1
        if word_frequency == window_char_frequency:
            count += 1
    return count


if __name__ == "__main__":
    print(CountOccurrence('aabaabaa', 'aaba'))
