'''
Depth first search

function DFS(root):
    if root == NULL:
        return;
    root.visited = true;

    for child in root:
        if child.visited == false:
            DFS(child)

}
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

def DFS(root):
    if root is None:
        return
    root.visited = True;

    for child in root.children:
        if child.visited == False:
            DFS(child)





g = Node(0)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(1, 6)
print(g.children)