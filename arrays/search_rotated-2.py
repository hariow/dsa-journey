# Search in Rotated Sorted Array-2

# Brute Force Solution

nums=[1,2,2,3,3,4,4,7,5,6,8,9]
#     0 1 2 3 4 5 6
def search(nums):
    n=len(nums)
    target=3

    for i in range(0,n):
        if nums[i]==target:
            return True
    return False

print(search(nums))


# Optimal Solution

nums=[17,18,20,1,3,4,7,6,8,9,10,11,12,13]
#     0  1  2  3 4 5 6 7 8 9 10 11 12 13
def search(nums):
    n=len(nums)
    target=4
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        
        if nums[mid]==nums[low]==nums[high]:
            low+=1
            high+=1
            continue

        if nums[mid]<=nums[high]:
            if nums[mid]<=target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
        else:
            if nums[low]<=target<=nums[mid]:
                high=mid-1
            else:
                low=mid+1
    return False

print(search(nums))
