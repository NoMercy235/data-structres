"""
Please delete a given node from a singly-linked list.
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, root: Node):
        self.root = root

    def single(self):
        return self.root.next is None

    def display(self):
        current = self.root
        while current:
            print(str(current.val) + (' --> ' if current.next is not None else ''), end='')
            current = current.next
        print()
        return self

    def delete_node(self, node: Node):
        if self.single() and self.root.val == node.val:
            self.root = None
            return self
        elif self.root.val == node.val:
            self.root = self.root.next
            return self

        last = self.root
        current = self.root.next
        while last.next is not None:
            if current.val == node.val:
                last.next = current.next
            last = current
            current = current.next

        return self


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    linked_list = LinkedList(a)

    linked_list \
        .display() \
        .delete_node(d) \
        .display() \
        .delete_node(b) \
        .display() \
        .delete_node(a) \
        .display() \
        .delete_node(c) \
        .display() \
        .delete_node(e) \
        .display()
