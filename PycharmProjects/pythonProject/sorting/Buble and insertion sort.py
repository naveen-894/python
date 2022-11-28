def buble_sort(data):
    nums=list(data)

    for _ in range (len(nums)-1):
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]

    return  nums

def insertionSort(data):
    nums=list(data)
    for i in range(len(nums)):
        element=nums.pop(i)
        j=i-1
        while j>=0 and element<nums[j]:
            j-=1
        nums.insert(j+1,element)
    return nums

# print(insertionSort([33,67,6,78,44,4]))
print(insertionSort([33]))


for i in range(10):
    print (i)