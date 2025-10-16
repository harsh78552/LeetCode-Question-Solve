def BulbSwitcher(target):
    count = 1
    if target == 0:
        return 0
    elif target == 1:
        return 1
    else:
        for j in range(2, target + 1):
            if j ** 2 <= target:
                count += 1
            else:
                break
    return count


print(BulbSwitcher(int(input())))
