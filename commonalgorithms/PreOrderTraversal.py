'''
pre-order traversal
'''

def preOrder(node):
    if not node:
        print(str(node.data) + ' ')
        preOrder(node.left)
        preOrder(node.right)