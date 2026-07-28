# Floor & Ceil in Sorted Array 

nums=[3,4,4,4,8,9,9,10,12,12,14,15]
#     0 1 2 3 4 5 6 7  8  9  10  11
def floor_ceil(nums):
    n=len(nums)
    target=6

    floor=-1
    ceil=-1
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]>target:
            ceil=nums[mid]
            high=mid-1
        else:
            floor=nums[mid]
            low=mid+1
    return[floor,ceil]

print(floor_ceil(nums))


