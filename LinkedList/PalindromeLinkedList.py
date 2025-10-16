def PalindromeLinkedList(head):
    stack = []
    cur = head
    while cur:
        stack.append(cur.val)
        cur = cur.next

    cur = head
    while cur:
        x = stack.pop()
        if cur.val != x:
            return False
        cur = cur.next
    return True


if __name__ == "__main__":
    print(PalindromeLinkedList([1, 2, 2, 1]))
