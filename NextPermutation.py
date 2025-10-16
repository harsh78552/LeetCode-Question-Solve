def NextPermutation(array):
    permutationMake = 1
    for num in range(1, len(array) + 1):
        permutationMake *= num
    for _ in range(permutationMake):
        pass




if __name__ == "__main__":
    print(NextPermutation([1, 2, 3]))
