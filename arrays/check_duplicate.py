# Remove Duplicates from a Sorted Array

nums=[1,2,2,3,4,4,6,9,10]
#     i j
n=len(nums)
def rmv_dup(nums,n):
    if n==1:
        return 1
    i=0
    j=i+1

    for j in range(1, n):
            if nums[j]!=nums[i]:
                i+=1
                nums[j],nums[i]=nums[i],nums[j]
            j+=1 

    return i+1     # i+1=k


k = rmv_dup(nums, n)
print(nums[:k])