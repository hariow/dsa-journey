##  Asteroid Collision

nums=[4,7,1,1,2,-3,-7,17,15,-16]

n=len(nums)
stack=[]

for i in range(0,n):
    if nums[i]>0:
        stack.append(nums[i])
    else:
        while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(nums[i]):
            stack.pop()
        if len(stack)!=0 and stack[-1]==abs(nums[i]):
            stack.pop()
        elif len(stack)==0 or stack[-1]<0:
            stack.append(nums[i])

print(stack)