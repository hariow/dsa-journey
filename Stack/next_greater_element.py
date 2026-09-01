## Monotonic Stack Approach - Next Greater Element

# Brute Force 

nums=[19,4,2,11,6,5,3,10]
#      i j
n=len(nums)
ans=[-1]*n

for i in range(0,n):
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            ans[i]=nums[j]
            break
    
print(ans)


## Optimal Solution ( Monotonic Stack)

nums=[19,2,4,9,3,5,8,10]
#                     i 
n=len(nums)
ans=[-1]*n
stack=[]

for i in range(n-1,-1,-1):
    while len(stack)!=0 and stack[-1]<=nums[i]:
        stack.pop()

    if len(stack)!=0:
        ans[i]=stack[-1]
        
    stack.append(nums[i])

print(ans)