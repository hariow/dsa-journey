# Next Greater Element - 2

## Optimal Monotonic-Stack Solution

nums=[19,4,2,11,6,5,3,10]
#                   i    
n=len(nums)
ans=[-1]*n  # initialize answer list with -1
stack=[]    # stack used to store potential next greater elements

for i in range(2*n-1,-1,-1):

    # pop elements smaller than or equal to the current element
    while len(stack)!=0 and stack[-1]<=nums[i%n]: 
        stack.pop()

    if i<n:
        if len(stack)!=0:
            ans[i]=stack[-1]
        
    stack.append(nums[i%n])  # add current element to the stack

print(ans)
