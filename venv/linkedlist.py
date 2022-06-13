class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "{0.data}".format(self)

class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return None
        self.tail.next = Node(data)
        self.tail = self.tail.next
        return None

    def delete(self, data = None):
        if data is None:
            return None

        return None

    def search(self, data):
        return None

    def printNode(self):
        temp = self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next
        return None

class doublelinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.prev = None
            self.tail = self.head
            return None
        self.tail.prev = self.tail
        self.tail = Node(data)
        return None

    def delete(self, data = None):
        if data is None:
            return None

        return None

    def search(self, data):
        return None

    def printNode(self):
        temp = self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next
        return None

llist =  linkedList()
llist.insert(5)
llist.insert(9)
llist.printNode()


