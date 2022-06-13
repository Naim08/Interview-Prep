'''
Breath first search


'''

class Graph:
    def __init__(self):
        self.val = 0

class Node:
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.children = []

    def addEdge(self, vertice, val):
        if vertice == self.val:
            self.children.append(Node(val))
            return

        for child in self.children:
            child.addEdge(vertice, val)

def BFS(root):
    if root is None:
        return

    q = [root]

    while len(q) != 0:
        node = q.pop()

        if node.visited == True:
            continue

        print(node.val)
        node.visited == True

        for child in node.children:
            q.append(child)





g = Node(0)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(1, 6)
print(BFS(g))