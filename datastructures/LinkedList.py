class LinkedList:
    def __init__(self):
        self.node = Node()
        
    def add(self, data):
        if self.node.next is None:
            self.node.next = Node(data)
        else:
            self.node = self.node.next
    

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None    # for double linkedlist

