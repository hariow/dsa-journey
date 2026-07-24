# Maximum Subarray Sum

# Brute Force
nums=[1,2,4,7,5,8,10]

def max_arrsum(nums):
    n=len(nums)
    maximum=float('-inf')

    for i in range(0,n):
        total=0
        for j in range(i,n):
            total+=nums[j]

            if total>maximum:
                maximum=total
    return maximum

print(max_arrsum(nums))


# Optimal Solution

nums=[-1,2,4,-7,5,8,10]

def max_arrsum(nums):
    n=len(nums)
    maximum=float('-inf')
    total=0

    for i in range(0,n):
            total+=nums[i]
            if total>maximum:
                maximum=total
            if total<0:
                total=0
    return maximum

print(max_arrsum(nums))