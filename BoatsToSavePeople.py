def BoatsToSavePeople(people, limit):
    people.sort()
    count = 0
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        count += 1
    return count


print(BoatsToSavePeople([3, 3, 4, 5], 5))
# print(BoatsToSavePeople([3, 2, 2, 1], 3))
# print(BoatsToSavePeople([1, 2], 3))
