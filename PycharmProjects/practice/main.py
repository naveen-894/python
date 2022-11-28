def linear_search(array,target):
    index=0
    while index<len(array):
        if array[index]==target:
            return index
        index+=1
    return -1

def binary_search(array,target,start=0,end=None):
    if end is None:
        end=len(array)
    mid=(start+end)//2
    if start>end:
        return -1
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return  binary_search(array,target,mid+1,end)


class binary_tree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
    def height(self):
        if self is None:
            return 0
        return 1+max(binary_tree.height(self.left),binary_tree.height(self.right))
    def size(self):
        if self is None:
            return 0
        return 1+binary_tree.size(self.left)+binary_tree.size(self.right)
    def traverse_in_order(self):
        if self is None:
            return []
        return binary_tree.traverse_in_order(self.left)+[self.key]+binary_tree.traverse_in_order(self.right)
    def tree_to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return (binary_tree.tree_to_tuple(self.left),self.key,binary_tree.tree_to_tuple(self.right))
    def is_min_max(self):
        if self is None:
            return 0,0
        min_l,max_l=binary_tree.is_min_max(self.left)
        min_r,max_r=binary_tree.is_min_max(self.right)
        minimum=min(min_r,self.key,min_l)
        maximum=max(max_r,self.key,max_l)
        return minimum,maximum

def convert_to_binary_tree(data):
    if isinstance(data,tuple) and len(data)==3 :
        node=binary_tree(data[1])
        node.left=convert_to_binary_tree(data[0])
        node.right=convert_to_binary_tree(data[2])
    elif data is None:
        node=None
    else:
        node=binary_tree(data)
    return node

def buble_sort(array):
    for _ in range(len(array)-1):
        for i in range (len(array)-1):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
    return array

def insertion_sort(array):
    for i in range(len(array)):
        value=array.pop(i)
        j=i-1
        while j>=0 and value<array[j]:
            j-=1
        array.insert(j+1,value)
    return array

def sort_array(nums1,nums2):
    i,j,merge_array=0,0,[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merge_array.append(nums1[i])
            i+=1
        else:
            merge_array.append(nums2[j])
            j+=1
    return merge_array+nums2[j:]+nums1[i:]

def merge_sort(array):
    if len(array)<2:
        return  array
    mid=len(array)//2
    left,right=merge_sort(array[:mid]),merge_sort(array[mid:])
    return sort_array(left,right)

print(merge_sort([4,1,3,5,2,7,9,3]))
tree=convert_to_binary_tree(((None,4,5),4,(None,4,(6,8,None))))
print(tree.is_min_max())

print(binary_search([1,2,3,4,5,6],4))