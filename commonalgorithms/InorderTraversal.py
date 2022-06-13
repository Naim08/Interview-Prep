'''
Inorder Traversal Algo
'''

from datastructures.tree import tree



def inOrder(t: tree):
    if t.root != None:
        inOrder(t.left)
        print(t.root.data)
        inOrder(t.right)

t = tree(15)

t.add(10)
t.add(20)
t.add(5)
t.add(11)
t.add(16)

print(t.root.left.data)
print(t.root.left.left.data)
print(t.root.left.right.data)

t.printTree('inOrder')
t.printTree('preOrder')
