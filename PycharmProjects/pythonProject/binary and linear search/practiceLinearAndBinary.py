testCases=[
    {
    'num':[3,4,5,6,7,8,8,8,1,2],
    'outPut':7
},
{
    'num':[6,7,7,7,8,1,2],
    'outPut':4
},
{
    'num':[],
    'outPut':0
},
{
    'num':[2],
    'outPut':0
},
{
    'num':[5,6,7,8,1],
    'outPut':0
},
]

def linearSearch(array):

    position=0
    while position<len(array):
        if position>0 and array[position]<array[position-1]:
            return position-1
        position+=1

    return 0

for input in testCases:
    result=linearSearch(input["num"])
    print(result)


def binarySearch(array):
    firstIndex,lastIndex=0,len(array)-1
    while firstIndex<lastIndex:
        mid=(firstIndex+lastIndex)//2
        if mid>0 and array[mid]>array[mid+1]:
            return mid
        if array[mid]>array[lastIndex]:
            firstIndex=mid
        elif array[mid]<array[firstIndex]:
            lastIndex=mid
    return 0

for input in testCases:
    result1=binarySearch(input['num'])
    print(result1)


