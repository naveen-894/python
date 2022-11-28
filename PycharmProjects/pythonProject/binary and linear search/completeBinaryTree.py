class binary_tree:
    def __init__(self,key):
        self.key,self.left, self.right=key,None,None
    def height(self):
        if self is None:
            return 0
        return 1+(max(binary_tree.height(self.left),binary_tree.height(self.right)))
    def size(self):
        if self is None:
            return 0
        return 1+binary_tree.size(self.left)+binary_tree.size(self.right)

    def traverse_inorder(self):
        if self is None:
            return []
        return (binary_tree.traverse_inorder(self.left)+[self.key]+binary_tree.traverse_inorder(self.right))
    def tree_to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        print(self.key)

        return binary_tree.tree_to_tuple(self.left),self.key,binary_tree.tree_to_tuple(self.right)

    def parse_tuple(data):
        if data is None:
            node=None
        elif isinstance(data,tuple) and len(data)==3:
           node=binary_tree(data[1])
           node.left=  binary_tree.parse_tuple(data[0])
           node.right=  binary_tree.parse_tuple(data[2])
        else:
            node=binary_tree(data)

        return node
    def isBst_min_max(self):
        if self is None:
            return True,None,None

        is_bst_l,min_l,max_l=binary_tree.isBst_min_max(self.left)
        is_bst_r,min_r,max_r=binary_tree.isBst_min_max(self.right)

        _is_bst_node=(max_l is None or max_l>self.key) and  ( min_l is None or min_r<self.key ) and (is_bst_r and is_bst_l)
        min_bst=min(binary_tree.removeNone([min_r,min_l,self.key]))
        max_bst = max(binary_tree.removeNone([max_r, max_l, self.key]))
        print(_is_bst_node,min_bst,max_bst)

        return _is_bst_node,min_bst,max_bst

    def removeNone(nums):
        return (x for x in nums if x is not None)

    def insert(self,value):#it will not update just insert in one after other
        if self is None:
           self=binary_tree(value)
        elif value<self.key:
            self.left=binary_tree.insert(self.left,value)
        else:
           self.right= binary_tree.insert(self.right,value)

        return self

    def find(self,value):
        if self is None:
            return None
        elif self.key==value:
            return self
        elif value<self.key:
            return binary_tree.find(self.left,value)
        else:
            return binary_tree.find(self.right,value)

    def update(self,key,value):
        target=binary_tree.find(self,key)
        if target is not None:
            target.key=value

    def is_balanced_bst(self):
        if self is None:
            return True,0
        isBst_l,height_l=binary_tree.is_balanced_bst(self.left)
        isBst_r,height_r=binary_tree.is_balanced_bst(self.left)

        is_bst=isBst_l and isBst_r and abs(height_l-height_r)<=1

        height=1+max(height_r,height_l)

        return is_bst,height
    def make_balanced_bst(data,low,high):
        if high is None:
            high=len(data)-1
        if low>high:
            return None
        mid=(low+high)//2
        root =binary_tree(data[mid])
        root.left=binary_tree.make_balanced_bst(data,low,mid-1)
        root.right=binary_tree.make_balanced_bst(data,mid+1,high)

        return root

    def balance_bst(tree):
        return binary_tree.make_balanced_bst(binary_tree.traverse_inorder(tree))

# class bst_python():
#     def __init__(self):
#         self.root=None
#
#     def __setitem__(self, key,value):




# tuple1=((1,3,None),2,((None,3,4),5,(6,7,8)))
# tree=binary_tree.parse_tuple(6)

# result=tree.tree_to_tuple();
# print(tree.isBst_min_max())
# print(tree.tree_to_tuple())
# tree.insert(8)

# print(tree.height())
# print(tree.tree_to_tuple())
# print(tree.find(8))
# tree.update(8,7)
# print(tree.right.key)
#
# print(tree.is_balanced_bst())

print(binary_tree.make_balanced_bst([1,2,3,4,5,6,7,8],0,7))

print(binary_tree.traverse_inorder(  binary_tree.make_balanced_bst([1,2,3,4,5,6,7,8],0,7)))









