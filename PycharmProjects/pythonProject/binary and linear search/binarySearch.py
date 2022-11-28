def findIndex(array,searchTerm):
    firstIndex, lastIndex = 0, len(array) - 1

    def binarySearch(firstIndex,lastIndex,condition):
        while firstIndex<=lastIndex:
            mid=(firstIndex+lastIndex)//2
            result=condition(mid)
            if result=='found':
                return mid
            elif result=='right':
                lastIndex=mid-1
            else:
                firstIndex=mid+1
        return -1

    def checkRepeating(mid):
        if array[mid]==searchTerm:
            if mid>0 and array[mid-1]==searchTerm:
                return 'left'
            else:
                return 'found'
        elif array[mid]<searchTerm:
            return 'left'
        else:
            return 'right'
    return binarySearch(firstIndex,lastIndex,checkRepeating)


input=[
    {
        'testArray':[1,2,3,4,5,6,7,8],
        'searchTerm':1
    },
    {
        'testArray': [1, 2, 3, 4, 5, 6, 7, 8],
        'searchTerm': 8
    },
    {
        'testArray': [1, 2, 3, 4, 5, 6, 7],
        'searchTerm': 4
    },
    {
        'testArray': [1, 2, 3, 4, 5, 6, 7, 8],
        'searchTerm': 8
    },
    {
        'testArray': [],
        'searchTerm': 10
    },
]

for testCase in input:
    result=findIndex(testCase['testArray'],testCase['searchTerm'])
    print(result)