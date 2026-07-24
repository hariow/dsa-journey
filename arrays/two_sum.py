#Two sum problem

# Brute Force

nums=[1,2,3,4,5,6,7,8,9,10]
#     0 1 2 3 4 5 6 7 8 9

def two_sum(nums):
    n=len(nums)
    target=10
    for i in range(0,n-1):
        for j in range(i + 1, n):
                   if nums[i]+nums[j]==target:
                    return [i,j]
                   
                     
    return -1   

print(two_sum(nums))        


# Optimal Solution

nums=[1,2,3,4,5,6,7,8,9,10]
#     0 1 2 3 4 5 6 7 8 9

def two_sums(nums):
    n=len(nums)
    hash_map={}
    target=10

    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]

        hash_map[nums[i]]=i

print(two_sums(nums))
    
