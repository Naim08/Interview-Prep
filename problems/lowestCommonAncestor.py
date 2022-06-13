'''

Given values of two values n1 and n2 in a Binary Search Tree, find the Lowest
Common Ancestor (LCA).
You may assume that both the values exist in the tree.

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = Node(20)
    
    def add(self, data):
        if (self.root == None):
            self.root = Node(data)
        else:
            self._add(data, self.root)
    
    def _add(self, data, node):
        if (data < node.data):
            if (node.left != None):
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if (node.right != None):
                self._add(data, node.right)
            else:
                node.right = Node(data)


def lowestCommonAncestor(root, n1, n2):
    # Base Case
    if root is None:
        return None
    
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if (root.data > n1 and root.data > n2):
        return lowestCommonAncestor(root.left, n1, n2)
        
        # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if (root.data < n1 and root.data < n2):
        return lowestCommonAncestor(root.right, n1, n2)
    
    return root


tree = BST()

tree.add(10)
tree.add(5)
tree.add(25)

print(tree.root.left.data)
print(tree.root.right.data)
