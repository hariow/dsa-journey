#Finding Missing No.

# Brute Force
nums=[1,0,3,4,5]

n=len(nums)

def msg(nums,n):
    for i in range(0,n+1):
        if i not in nums:

           return i

print(msg(nums, n))


#Better solution

nums=[1,0,3,4,5]

def msgno(nums,n):
    n=len(nums)
    freq={}

    for i in range(0,n+1):
        freq[i]=0
    for j in nums:
        freq[j]=1
    for k,v in freq.items():
        if v==0:
            return k
        
print(msgno(nums,n))


# Optimal Solution

nums = [1,0,3,4,5]

def msgno(nums):
    n = len(nums)

    actual_sum = 0
    for i in range(n):
        actual_sum += nums[i]

    expected_sum = n*(n + 1)//2

    return expected_sum - actual_sum

print(msgno(nums))