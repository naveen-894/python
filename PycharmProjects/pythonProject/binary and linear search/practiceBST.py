class bst:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
    def height(self):
        if self is None:
            return 0
        return 1+max(bst.height(self.left),bst.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1+bst.size(self.left)+bst.size(self.right)
    def travers_in_order(self):
        if self is None:
            return []
        return (bst.travers_in_order(self.left)+[[self.key,self.value]]+bst.travers_in_order(self.right))

    def tupleToTree(self,data):
        if data is None:
            node=None
        elif(isinstance(data,tuple) and len(data)==3):
            node=bst.tupleToTree(data[1])
            node.left=bst.tupleToTree(data[0])
            node.right=bst.tupleToTree(data[2])

        else:
            node=bst(data)
        return node
    def treeToTuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return  self.key
        return(bst.treeToTuple(self.left),self.key,bst.treeToTuple(self.right))

    def isBst_min_max(self):
        if self is None:
            return True,None,None
        isbst_l,min_l,max_l=bst.isBst_min_max(self.left)
        isbst_r, min_r, max_r = bst.isBst_min_max(self.right)

        isbst=((isbst_r and isbst_l)and(min_l is None or self.key>min_l)and(max_r is None or self.key<max_r))
        minimum=min(bst.removeNone([min_r,self.key,min_l]))
        maximum=max(bst.removeNone([max_l,self.key,max_r]))

        return isbst,minimum,maximum

    def insert(self,key,value):
        if self is None:
            self = bst(key,value)
        elif(self.key>key):
            self.left=bst.insert(self.left,key,value)
        else:
            self.right=bst.insert(self.right,key,value)
        return  self

    def isBalanced_bst(self):
        if self is None:
            return True,0
        isbst_l,height_l=bst.isBalanced_bst(self.left)
        isbst_r, height_r = bst.isBalanced_bst(self.right)

        isbst=isbst_l and isbst_r and abs(height_l-height_r)<=1
        height=1+max(height_r,height_l)
        return isbst,height
    def make_balanced_bst(data,low,high):
        # if high is None:
        #     high=len(data)-1
        if low>high:
            return None

        mid=(low+high)//2
        node = bst(data[mid][0],data[mid][1])
        node.left = bst.make_balanced_bst(data, low, mid - 1)
        node.right = bst.make_balanced_bst(data, mid + 1, high)

        return node

    def removeNone(data):
        return (x for x in data if x is not None)

    def find(self,key):
        if self is None:
            return None
        elif key==self.key:
            return self
        elif key>self.key:
           return  bst.find(self.right,key)
        else:
           return  bst.find(self.left,key)

    def update(self,key,value):
        target=bst.find(self,key)
        print(target,'is the target value')
        if target is not None:
            target.value=value
            return target.value

    def arrange_balance_bst(self):
        sortedList=bst.travers_in_order(self)
        print(sortedList)
        return bst.make_balanced_bst(sortedList,0,len(sortedList)-1)



class treeMap:
    def __init__(self):
        self.root=None

    def __setitem__(self, key, value):
        node=bst.find(self.root,key)
        if node is None:
            self.root=bst.insert(self.root,key,value)
            data=bst.travers_in_order(self.root)
            self.root=bst.make_balanced_bst(data,0,len(data)-1)
        else:
            tuple(self.root,key,value)
    def __getitem__(self, key):
        node=bst.find(self.root,key)
        return  node.value if node else None
    def __iter__(self):
        return (x for x in bst.travers_in_order(self.root))
    def __len__(self):
        return bst.size(self.root)

# tree=bst.make_balanced_bst([{'key':1,'value':'naveen'},{'key':2,'value':'raghu'},{'key':3,'value':'naveen c shetty'},{'key':4,'value':'bagavan'}],0,3)
# print(tree.height())
# tree.insert(9,'ninga')
# print(tree.height())
# print(tree.right.right.right.value)
#
# print(tree.update(1,'naveena'))
# print(tree.travers_in_order())
# tree.arrange_balance_bst()

tree=treeMap()

tree[1]='naveenaaaaaaaaaaaaaa'
tree[6]='naveenaaaaaaaaalay'
tree[4]='naveenaaaa'
tree[5]='naaaa'
tree[8]='naveennn'
tree[2]='naveenaaaaaaaaaaaaaa'
tree[33]='naveenaaaaaaaaa'
tree[10]='naveenaaaa'
tree[58]='naaaa'
tree[7]='naveennn'
print(tree.root.value)
print(len(tree))

for key,value in tree:
    print(key,value)