#Implementation of Lower Bound

nums=[1,2,3,4,5,6,6,7,8,9,9,9]

def upper_bound(nums,target):
    n=len(nums)
    UB=n
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            UB=mid
            high=mid-1
    
        else:
            low=mid+1
                
    return UB
print(upper_bound(nums,9))
        