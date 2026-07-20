# Ascending Insertion Sort

nums=[9,8,7,6,5,4,3,2,1]

n=len(nums)

for i in range(1,n):
    key=nums[i]
    j=i-1

    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1

    nums[j+1]=key

print(nums)


# Descending Insertion Order

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]

n=len(nums)

for i in range(1,n):
    key=nums[i]
    j=i-1

    while j>=0 and nums[j] < key:
        nums[j+1]=nums[j]
        j-=1
    
    nums[j+1]=key

print(nums)
