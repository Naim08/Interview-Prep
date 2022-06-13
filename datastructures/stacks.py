class Stack:
    def __init__(self):
        self.container = []
        self.top = 0

    def pop(self):
        value = self.container[len(self.container) - 1]
        del self.container[len(self.container) - 1]
        return value

    def push(self, data):
        self.container.append(data)
        return None

    def peek(self):
        return self.container[len(self.container) - 1]