# second largest element in the array

nums=[55,32,97,-55,45,32,88,21]

n=len(nums)

largest=float('-inf')
sec_largest=float('-inf')

for i in range(0,n):
    if nums[i] > largest:
        largest=nums[i]
    if nums[i]>sec_largest and nums[i]!=largest:
        sec_largest=nums[i]

print(sec_largest)

# optimal solution (second method)

nums=[55,32,97,-55,45,32,88,21]

n=len(nums)

largest=float('-inf')
sec_largest=float('-inf')

for i in range(0,n):
    if nums[i]>largest:
        sec_largest=largest
        largest=nums[i]
    
    elif nums[i]>sec_largest and nums[i]!=largest:
        sec_largest=nums[i]

print(sec_largest)