def ParametrisedFactorialRecursion(factorial, num, approach):
    if num > approach:
        print(factorial)
        return
    ParametrisedFactorialRecursion(factorial * num, num + 1, approach)


ParametrisedFactorialRecursion(1, 1, 5)


def FunctionalFactorialRecursion(num):
    if num == 1:
        return 1
    return num * FunctionalFactorialRecursion(num - 1)


print(FunctionalFactorialRecursion(5))
