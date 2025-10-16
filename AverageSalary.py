def average(salary):
    salary.sort()
    total_sum = 0
    total_num = 0
    for num in range(1, len(salary) - 1):
        total_sum += salary[num]
        total_num += 1
    total_sum = total_sum / total_num
    return f"{total_sum:.5f}"


print(average([4000, 3000, 1000, 2000]))
