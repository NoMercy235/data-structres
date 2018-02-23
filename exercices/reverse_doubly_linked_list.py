"""
Reverse a doubly linked list.
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self, root: Node):
        self.root = root

    def reverse(self):
        if self.root.next is None:
            return

        current = self.root
        while current:
            current = current.next
            current.previous.next = current.previous.previous
            current.previous.previous = current
            if current.next is None:
                current.next = current.previous
                current.previous = None
                self.root = current
                current = None

    def display(self):
        current = self.root
        while current:
            print(str(current.val) + (' <--> ' if current.next is not None else ''), end='')
            current = current.next
        print()
        return self


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.previous = a
    b.next = c
    c.previous = b
    c.next = d
    d.previous = c
    d.next = e
    e.previous = d

    linked_list = DoublyLinkedList(a)

    linked_list.display()

    linked_list.reverse()

    linked_list.display()