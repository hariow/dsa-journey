## Ascending Sorting

nums=[9,8,7,6,5,4,3,2,1]

def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_ind=i
        for j in range(i+1,n):
            if nums[j]<nums[min_ind]:
                min_ind=j
        nums[i],nums[min_ind]=nums[min_ind],nums[i]

(selection_sort(nums))
print(nums)

## Descending Sorting

nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        max_ind=i
        for j in range(i+1,n):
            if nums[j]>nums[max_ind]:
                max_ind=j
        nums[i],nums[max_ind]=nums[max_ind],nums[i]

selection_sort(nums)

print(nums)