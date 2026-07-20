## Ascending Bubble Sort

nums=[9,8,7,6,5,4,3,2,1]

n=len(nums)

for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)


## Descending Bubble Sort

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]

n=len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j+1]>nums[j]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)