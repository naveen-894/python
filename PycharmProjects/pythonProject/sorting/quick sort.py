def QuickSort(nums,start=0,end=None):
    if end is None:
        end=len(nums)-1
    print(start,end)

    if start<end:
        print(nums)
        pevit=partion(nums,start,end)
        QuickSort(nums,start,pevit-1)
        QuickSort(nums,pevit+1,end)
    return nums
def partion(nums,start,end):
    if end is None:
        end=len(nums)-1
    l,r=start,end-1

    while l<r:
        if nums[l]<=nums[end]:
            l+=1
        elif nums[r]>nums[end]:
            r-=1
        else:
            nums[l],nums[r]=nums[r],nums[l]
    if nums[l]>nums[end]:
            nums[l],nums[end]=nums[end],nums[l]
    return l

print(QuickSort([7,3,0,11,5,9,33,7,1,4]))



    
