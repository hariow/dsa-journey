# brute force solution 

nums=[1,2,3,4,5,6,7,8,9]
#                   i    
n=len(nums)
k=3
rotations=k%n

for _ in range(0,rotations):
    e=nums.pop()
    nums.insert(0,e)

print(nums)


# with slicing

nums=[1,2,3,4,5,6,7,8,9]
k=3
n=len(nums)
k=n%k

nums[:]=nums[n-k] + nums[:n-k]

print(nums)


# Optimal Solution

nums=[1,2,3,4,5,6,7,8,9]
k=3
k=n%k
n=len(nums)
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

    reverse(n-k,n-1) # reverse Lost k element 
    reverse(0,n-k-1) # reverse remaninig element
    reverse(0,n-1)   # reverse whole array