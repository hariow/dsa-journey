#right rotating array using slicing

nums=[1,2,3,4,5,6,7,8]

n=len(nums)

nums[:]=[nums[n-1]]+nums[0:n-1]


print(nums)


#right rotating array without slicing

nums=[1,2,3,4,5,6,7,8,9]
#                   i
n=len(nums)

temp=nums[n-1] # 9
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]

nums[0]=temp

print(nums)
