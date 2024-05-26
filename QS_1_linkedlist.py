class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def printList(self, head):
        current = head
        while current:
            print(current.val, end = " ")
            current = current.next
        print()

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nextnum = curr.next
            curr.next = prev
            prev = curr
            curr = nextnum
        return prev


new_ = LinkedList()
new_.append(1)
new_.append(2)
new_.append(3)
new_.append(4)
new_.append(5)
# new_.printList(new_.head) 
reversed_head = new_.reverse(new_.head)
new_.printList(reversed_head)  