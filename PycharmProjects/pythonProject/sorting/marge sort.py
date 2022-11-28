def merge_sort(nums):
    if len(nums)<2:
        return nums
    mid=len(nums)//2

    left_sort,right_sort=merge_sort(nums[:mid]),merge_sort(nums[mid:])

    return merge(left_sort,right_sort)

def merge(nums1,nums2):
    i,j,mergeNums=0,0,[]

    while i<len(nums1) and j<len(nums2):

        if nums1[i]<nums2[j]:
            mergeNums.append(nums1[i])
            i+=1
        else:
            mergeNums.append(nums2[j])
            j+=1
    return mergeNums+nums2[j:]+nums1[i:]


print(merge_sort([4,4,1,2,7,5,8,7,2,-1,0]))