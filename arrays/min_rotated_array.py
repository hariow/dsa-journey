# Find Minimum In Rotated Sorted Array

nums=[1,0,3,6,4,8,7,9,10]

n=len(nums)
mini=float('inf')

for i in range(0,n):
    mini=min(nums[i],mini)

print(mini)


# Optimal Solution

nums=[7,8,9,1,2,3,4]
#     0 1 2 3 4 5 6

def minielement(nums):
    n=len(nums)
    low=0
    high=n-1
    mini=float('inf')

    while low<=high:
        mid=(low+high)//2

        if nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1
        else:
            mini=min(mini,nums[low])
            low=mid+1
    return mini

print(minielement(nums))