# Find First & Last Occurrence in Sorted Array

# Brute Force Solution

nums=[1,2,3,3,3,3,5,6,8,9,9,10]
#     0 1 2 3 4 5 
def first_last(nums):
    n=len(nums)
    first=-1
    last=-1
    target=3

    for i in range(0,n):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i

    return [first,last]

print(first_last(nums))
           

# Optimal Solution

# Lower Bound & Upper Bound

nums = [1,2,3,3,3,3,5,6,8,9,9,10]

def lower_bound(nums, target):   # First index where nums[idx] >= target
    n = len(nums)
    low = 0
    high = n - 1
    lb = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upper_bound(nums, target):   # First index where nums[idx] > target
    n = len(nums)
    low = 0
    high = n - 1
    ub = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub-1


target = 3

print("Lower Bound Index :", lower_bound(nums, target))
print("Upper Bound Index :", upper_bound(nums, target))



