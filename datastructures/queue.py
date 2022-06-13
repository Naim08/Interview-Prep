class Queue:
    def __init__(self, size):
        self.container = [None for _ in range(size)]
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = size

    def enqueue(self, value):
        self.rear = (self.rear + 1) % self.capacity
        self.container[self.rear] = value
        self.size += 1
        return None

    def dequeue(self):
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return None

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        print(self.container[self.front])
        return None

    def __repr__(self):
        return "{0}".format(self.container)


q = Queue(10)
q.enqueue(5)
q.enqueue(4)
print(q.front)
print(q.rear)
q.dequeue()
print(q.front)
print(q.rear)
print(q)