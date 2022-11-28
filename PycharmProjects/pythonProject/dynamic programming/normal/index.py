def count_substr(str1,str2,index1=0,index2=0):
    if index1==len(str1)or index2== len(str2):
        return 0
    elif str1[index1]==str2[index2]:
        return 1+count_substr(str1,str2,index1+1,index2+1)
    else:
        return max(count_substr(str1,str2,index1+1,index2),count_substr(str1,str2,index1,index2+1))


# better than aboveone

def count_substring(str1,str2):
    memo={}
    def recurse(index1=0,index2=0):
        print(index1,index2)
        key=(index1,index2)
        if key in memo:
            return memo[key]
        elif index1 == len(str1) or index2 == len(str2):
            memo[key]=0
        elif str1[index1] == str2[index2]:
            memo[key]= 1 + recurse(index1 + 1, index2 + 1)
        else:
            memo[key]= max(recurse(index1 + 1, index2), recurse(index1, index2 + 1))
        return memo
    return recurse(0,0)

#problem:given n elements,each of which has a weight  and profit. determine the maximum profit that can be obtained by
# selecting the subset of the elements no more than capacity

def maximum_profit_recursive(wieghts,profits,capacity,index=0):
    if index==len(wieghts):
        return 0
    elif wieghts[index]>capacity:
        return maximum_profit_recursive(wieghts,profits,capacity,index+1)
    else:
        option1=maximum_profit_recursive(wieghts,profits,capacity,index+1)
        option2=profits[index]+maximum_profit_recursive(wieghts,profits,capacity-wieghts[index],index+1)
        return max(option1,option2)

# print(count_substring('naveen','srinath'))
print(max('nav','nav'))

print(maximum_profit_recursive([23,31,29,44,53,38,63,85,89,82],[92,57,49,68,60,43,67,84,87,72],165))

