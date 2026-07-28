# Introduction to Binary Search

# Iterative Solution

nums=[1,2,3,4,5,6,7,8,9,10]
#     0 1 2 3 4 5 6 7 8,9
def binary_search(nums,target):   # Time Complexity--> log_2(N)
    n=len(nums)
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binary_search(nums,9))       


# Recursive Solution

nums=[1,2,3,4,5,6,7,8,9,10]
#     0 1 2 3 4 5 6 7 8,9
def binary_search(nums,low,high): # Time Complexity--> log_2(N)
    if low>high:
        return -1
    target=9
    mid=low+high//2

    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        binary_search(nums,low+1,high)
    else:
        binary_search(nums,low,mid-1)
    

        


    