class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SinglyLinkedlist:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        self.count = 0
        if self.head is None:
            print('linked list is empty..')
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                self.count += 1
                current = current.next

    def middle(self):
        mid = self.count // 2
        current = self.head
        count = 0
        while current is not None and count < mid:
            count += 1
            current = current.next
        return current.data


sll = SinglyLinkedlist()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append([1, 2, 3, 4, 5, 6, 7, 8])
sll.append(5)
sll.append(6)
sll.traverse()
# print(sll.middle())
