class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.head = self.tail = self.size = 0

    def enqueue(self, value):
        if self.size == len(self.queue):
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % len(self.queue)
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return False
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % len(self.queue)
        self.size -= 1
        return value

    def front(self):
        if self.size == 0:
            return -1
        return self.queue[self.head]

    def rear(self):
        if self.size == 0:
            return -1
        return self.queue[self.tail - 1]

    def isEmpty(self):
        return self.size == 0


q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  
q.enqueue(4)
print(q.front())  
print(q.rear()) 