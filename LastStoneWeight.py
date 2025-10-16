from queue import PriorityQueue as pq


def LastStoneWeight(stones):
    new_data = pq()
    for num in stones:
        new_data.put(-num)
    while new_data.qsize() > 1:
        x = abs(new_data.get())
        y = abs(new_data.get())
        if x != y:
            new_data.put(-(x - y))
    return - (new_data.get()) if not new_data.empty() else 0


print(LastStoneWeight([2, 7, 4, 1, 8, 1]))
