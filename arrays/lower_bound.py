#Implementation of Lower Bound

nums=[1,2,3,4,5,6,6,7,8,9,9,9]

def lower_bound(nums,target):
    n=len(nums)
    LB=-1
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            LB=mid
            high=mid-1

        else:
            low=mid+1
            
    return LB
print(lower_bound(nums,9))
    

