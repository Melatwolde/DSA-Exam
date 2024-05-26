class first:
    def __init__(self, x):
        self.val = x
        self.next = None
class linked:
    def __init__(self):
        self.head = None
    def append(self, value):
            if not self.head:
                self.head = first(value)
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = first(value)


    def revers(self, head):
        prev = None
        curr = head

        while curr:
            nextnum = curr.next
            curr.next = prev
            prev = curr
            curr = nextnum
        return prev


ll = linked()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.printList(ll.head) 
reversed_head = ll.reverse(ll.head)
ll.printList(reversed_head)