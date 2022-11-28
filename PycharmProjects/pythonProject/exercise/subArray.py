# input: [1,3,4,2,4,7,5,3,4]
# sum:10
# output:2,5

def subArray(nums,sum):
    i,j, s=0,0,0

    while j<len(nums)+1 and i<len(nums):
        if s==sum:
            return i,j
        elif s>sum:
            if i<len(nums):
                s-=nums[i]
            i+=1
        else:
            if j<len(nums):
                s+=nums[j]
            j+=1
    return None ,None

print(subArray([3,4,2,99,8,5,3,4],20))
