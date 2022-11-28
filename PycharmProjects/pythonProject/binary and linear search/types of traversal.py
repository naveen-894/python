

class binaryTree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

def binaryTreeFunc(data):
    if isinstance(data,tuple) and len(data)==3:
        node=binaryTree(data[1])
        node.left=binaryTreeFunc(data[0])
        node.right=binaryTreeFunc(data[2])
    elif data is None:
        node=None
    else:
     node=binaryTree(data)
    return node

tuple1=((1,3,None),2,((None,3,4),5,(6,7,8)))

# print(binaryTreeFunc(tuple1))

node=binaryTreeFunc(tuple1)

def inOrderTraversal(node):
    print(node)
    if node is None:
        return []
    return (inOrderTraversal(node.left)+[node.key]+inOrderTraversal(node.right))

result1=inOrderTraversal(node)

print(result1)

def treeHeight(node):

    if node is None:
        return 0
    height=1+max(treeHeight(node.left),treeHeight(node.right))
    print('node is',node.key)
    print(height)
    return height

height=treeHeight(node)
