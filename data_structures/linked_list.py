class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


l = LinkedList()
l.head = Node(1)
second = Node(2)
third = Node(3)
l.head.next = second
second.next = third
while l.head is not None:
    print(l.head.value, end=" ")
    l.head = l.head.next
