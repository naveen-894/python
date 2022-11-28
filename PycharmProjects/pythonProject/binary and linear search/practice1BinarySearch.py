testCases=[
    {
    'num':[3,4,5,6,7,8,8,8,1,2],
    'searchTerm':7,
    'outPut':3
},
  {
    'num':[3,4,5,6,7,8,8,8,1,2],
    'searchTerm':1,
    'outPut':8
},
{
    'num':[6,7,7,7,8,1,2],
'searchTerm':6,
    'outPut':4
},
{
    'num':[],
'searchTerm':6,
    'outPut':0
},
{
    'num':[2],
'searchTerm':2,
    'outPut':0
},
]

def binarySearch(array,searchValue):
    first,last=0,len(array)-1
    while first<last:
        mid=(first+last)//2
        # print(first,last )
        if array[mid]==searchValue:
            return mid
        elif  searchValue<=array[last] and array[mid]<=searchValue:
            first=mid
        else:
            last=mid
    return 0
for input in testCases:
    result=binarySearch(input['num'],input['searchTerm'])
    print(result)
