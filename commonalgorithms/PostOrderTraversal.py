'''
Post Order Tree Traversal
'''

def postOrder(node):
    if not node:
        postOrder(node.left)
        postOrder(node.right)
        print(str(node.data) + ' ')

