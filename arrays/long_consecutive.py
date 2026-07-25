# Longest Consecutive Sequence

# Brute Force Solution
nums=[1,101,2,100,99,3,98,97,102]
#     i
def cns(nums):
    n=len(nums)
    count=0
    max_count=0
    for i in range(0,n):
        num=nums[i]
        count=1
        while num+1 in nums:
            count+=1
            num=num+1

        max_count=(max(count,max_count))

    return max_count

print(cns(nums))


# Better Solution

nums=[1,101,2,100,99,3,98,97,102]
#     i
def cns(nums):
    n=len(nums)
    nums.sort()
    last_small=float('-inf')
    longest=0

    for i in range(0,n):
        num=nums[i]

        if num-1==last_small:
            count+=1
            last_small=num
        else:
            num!=last_small
            count=1
            last_small=num

        longest=max(count,longest)
    return longest
print(cns(nums))         


# Optimal Solution

nums=[1,101,2,100,99,3,98,97,102]
#     i
def cns(nums):
    n=len(nums)
    my_set=set()
    for i in range(0,n):
        my_set.add(nums[i])
    longest=0
    
    for j in my_set:       # so lets j=1 then j=0
        if j-1 not in my_set:
            x=j
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)

    return longest        

print(cns(nums))

