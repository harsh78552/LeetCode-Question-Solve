def LoopFibonacciSeries(range_):
    first_number = 0
    second_number = 1
    print(first_number)
    print(second_number)
    for _ in range(range_ - 2):
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
        print(next_number)


print(LoopFibonacciSeries(10))


def RecursionFibonacciSeries(range_, count=3, x=0, y=1, store_fibonacci=None):
    if store_fibonacci is None:
        store_fibonacci = [0, 1]
    if count > range_:
        print(store_fibonacci)
        return
    next_number = x + y
    store_fibonacci.append(next_number)
    RecursionFibonacciSeries(range_, count + 1, y, next_number, store_fibonacci)


RecursionFibonacciSeries(10)
