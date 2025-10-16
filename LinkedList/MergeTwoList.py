class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    @staticmethod
    def linked_list_creation(values):
        dummy_list = Node(0)
        head = dummy_list
        for value in values:
            head.next = Node(value)
            head = head.next
        return dummy_list.next


class UnsortedMergedLinkedList:
    @staticmethod
    def unsorted_merged_linked_list(list1, list2):
        dummy_node = Node(0)
        head = dummy_node
        while list1 and list2:
            head.next = list1
            list1 = list1.next
            head = head.next

            head.next = list2
            list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        else:
            head.next = list2
        return dummy_node


class SortedMergedLinkedList:
    @staticmethod
    def sorted_merged_lined_list(list1, list2):
        dummy_node = Node(0)
        current = dummy_node
        while list1 and list2:
            if list1.data <= list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy_node.next


class DeleteNodeLinkedList:
    @staticmethod
    def delete_node_linked_list(linkedlist, num):
        while linkedlist and linkedlist.data == num:
            linkedlist = linkedlist.next
        current = linkedlist
        while linkedlist and current.next:
            if current.next.data == num:
                current.next = current.next.next
            else:
                current = current.next
        return linkedlist


class RemoveDuplicateLinkedList:
    @staticmethod
    def remove_duplicate_linked_list(linkedlist):
        if not linkedlist:
            return None
        current = linkedlist
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return linkedlist


class AddTwoNumber:
    @staticmethod
    def add_two_number(list1, list2):

        if not list1 or not list2:
            return None
        dummy_node = Node(0)
        current = dummy_node
        carry = 0
        while list1 or list2:
            x = list1.data if list1 else 0
            y = list2.data if list2 else 0
            sum_ = x + y + carry
            carry = sum_ // 10
            d = sum_ % 10

            current.next = Node(d)
            current = current.next
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        if carry > 0:
            current.next = Node(carry)
        return dummy_node.next


class DoubleNumber:
    @staticmethod
    def double_number(linkedlist):
        reference = linkedlist
        collect_number = 0
        while reference:
            collect_number = collect_number * 10 + reference.data
            reference = reference.next
        collect_number = collect_number * 2
        dummy_node = Node(0)
        reference_ = dummy_node
        for j in str(collect_number):
            reference_.next = Node(int(j))
            reference_ = reference_.next
        return dummy_node.next


class PrintLinkedList:
    @staticmethod
    def print_linked_list(linkedlist):
        current = linkedlist
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


l1 = LinkedList()
create = LinkedList.linked_list_creation([1, 1, 2, 3])
create2 = LinkedList.linked_list_creation([5, 6, 7, 8])
# merged = UnsortedMergedLinkedList.unsorted_merged_linked_list(create, create2)
# merged = SortedMergedLinkedList.sorted_merged_lined_list(create, create2)
# DeleteNodeLinkedList.delete_node_linked_list(merged, 2)
# remove = RemoveDuplicateLinkedList.remove_duplicate_linked_list(create)
# add = AddTwoNumber.add_two_number(create, create2)
double = DoubleNumber.double_number(create)
PrintLinkedList.print_linked_list(double)
