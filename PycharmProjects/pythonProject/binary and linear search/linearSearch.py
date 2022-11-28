import of as of


def linearSearch(array,searchTerm):
    position=0
    while position<len(array):
        if array[position]==searchTerm:
            return position
        position+=1
    return -1

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
        'testArray': [1, 2, 3, 4, 5, 6, 7, 8],
        'searchTerm': 4
    },
    {
        'testArray': [1, 2, 3, 4, 5, 6, 7, 8],
        'searchTerm': 10
    },
    {
        'testArray': [],
        'searchTerm': 10
    },
]

for testCase in input:
    result=linearSearch(testCase['testArray'],testCase['searchTerm'])
    print(result)

print('hiraj'<'hemantj')