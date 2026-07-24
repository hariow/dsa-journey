# Linear Search

nums=[1,2,3,4,5,6,7]

def lin_srh(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return (i)
  
    return -1

print(lin_srh(nums,9))