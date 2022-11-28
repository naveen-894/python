class binaryTree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

# tree0=binaryTree(1)
# tree1=binaryTree(2)
# tree2=binaryTree(3)

# tree0.left=tree1
# tree0.right=tree2
#
# print(tree0.key)
# print(tree0.left.key)
# print(tree0.right.key)

# node0=binaryTree(2)
# node1=binaryTree(3)
# node2=binaryTree(5)
# node3=binaryTree(1)
# node4=binaryTree(3)
# node5=binaryTree(7)
# node6=binaryTree(4)
# node7=binaryTree(6)
# node8=binaryTree(8)
#
# node0.left=node1
# node0.right=node2
#
# node1.left=node3
#
# node2.left=node4
# node2.right=node5
#
# node4.right=node6
#
# node5.left=node7
# node5.right=node8
#
# print(node2.right.key)

# function to binaryTree

def binaryTreeFunc(data):
    print(data)
    if isinstance(data,tuple) and len(data)==3:
        node=binaryTree(data[1])
        node.left=binaryTreeFunc(data[0])
        node.right=binaryTreeFunc(data[2])
        print('if ended')
    elif data is None:
        node=None
        print('elseif')
    else:
     node=binaryTree(data)
     print('else')
    return node
    print('end')

tuple1=((1,3,None),2,((None,3,4),5,(6,7,8)))

# print(binaryTreeFunc(tuple1))

node=binaryTreeFunc(tuple1)

print(node.right.right.key)