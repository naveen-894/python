# input1:'intention'
# input2:'exception'
# result:4


def minimum_edit_distance(str1,str2,i=0,j=0):
    if i==len(str1):
        return len(str2)-j
    elif j==len(str2):
        return len(str1)-i
    elif str1[i]==str2[i]:
        return minimum_edit_distance(str1,str2,i+1,j+1)
    else:
        return 1+min(
            minimum_edit_distance(str1,str2,i+1,j+1),#swap
            minimum_edit_distance(str1,str2,i+1,j),#delete
            minimum_edit_distance(str1,str2,i,j+1)#insert
        )



# using memo

def minimum_edit_memo(str1,str2):
    memo={}
    def recursion(i=0,j=0):
        key=i,j
        if key in memo:
            return memo[key]
        elif i==len(str1):
            memo[key]=len(str2)-j
        elif j==len(str2):
            memo[key]=len(str1)-i
        elif str1[i]==str2[j]:
            memo[key]= recursion(i+1,j+1)
        else:
            memo[key]= 1+min(recursion(i+1,j+1),recursion(i+1,j),recursion(i,j+1))
        return memo[key]
    return recursion(0,0)

# dynamic programming


def minimum_edit_dynamic(str1,str2,i=0,j=0):
    n1, n2 = len(str1), len(str2)
    table = [[0 for x in range(n2)] for x in range(n1)]

    for i in range(n1):
        print(table)
        for j in range(n2):
            if str2[j] == str1[i]:
                table[i][j] = table[i+1][j+1]
            else:

                table[i][j] =1+ min(table[i][j + 1], table[i + 1][j],table[i+1][j+1])
    print(table)
    return table[-1][-1]
print(minimum_edit_distance('intention','exception'))
print(minimum_edit_memo('intention','exception'))
print(minimum_edit_memo('saturday','sunday'))
print(minimum_edit_dynamic('intention','exception'))


