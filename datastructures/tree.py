
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class tree:
    def __init__(self, data):
        self.root = Node(data)

    def add(self, data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if(data < node.data):
            if(node.left != None):
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if(node.right != None):
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def _normalAdd(self, data, node):
        pass

    def find(self, data):
        if self.root == None:
            return None
        else:
           return self._find(self, data, self.root)

    def _find(self, data, node):
        if data == node.data:
            return node
        elif data < node.data and node.left != None:
            self._find(data, node.left)
        elif data > node.data and node.right != None:
            self._find(data, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self, traversal):
        if (self.root != None):
            if traversal == 'inOrder':
                self._printInTree(self.root)
            elif traversal == 'preOrder':
                self._printPreOrderTree(self.root)
            elif traversal == 'postOrder':
                self._printPostOrder(self.root)

    def _printInTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print(str(node.data) + ' ')
            self._printTree(node.right)

    def _printPreOrderTree(self, node):
        if (node != None):
            print(str(node.data) + ' ')
            self._printTree(node.left)
            self._printTree(node.right)

    def _printPostOrder(self, node):
        if not Node:
            self._printPostOrder(node.left)
            self._printPostOrder(node.right)
            print(str(node.data) + ' ')



