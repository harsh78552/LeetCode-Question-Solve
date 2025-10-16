def findKthLargest(nums,k):
    from queue import PriorityQueue as pq
    new_queue = pq()
    for num in nums:
        new_queue.put(-num)

    get_max = None
    for j in range(k):
        get_max = -new_queue.get()

    return get_max

print(findKthLargest([3,2,3,1,2,4,5,5,6],4))
