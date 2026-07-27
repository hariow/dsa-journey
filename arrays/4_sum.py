# Four Sum Solution

# Brute Force Solution

nums=[1,0,-1,0,-2,2]

def four_sum(nums):
    n=len(nums)
    if n<4:
        return 
    my_set=set()
    
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):    
                    if nums[i]+nums[j]+nums[k]+nums[l]==0:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    return[list(ans) for ans in my_set]
print(four_sum(nums))


# Better Solution

nums=[1,0,-1,0,-2,2]

def four_sum(nums):
    n=len(nums)
    if n<4:
        return
    target=0
    my_set=set()

    for i in range(0,n):
        for j in range(i+1,n):
            hash_set=set()
            for k in range(j+1,n):
                fourth=target-(nums[i]+nums[j]+nums[k])

                if fourth in hash_set:
                    temp=[nums[i],nums[j],nums[k],fourth]
                    temp.sort()
                    my_set.add(tuple(temp))             
                hash_set.add(nums[k])
    return [list(ans) for ans in my_set]       
print(four_sum(nums))


# Optimal Solution

nums=[1,0,-1,0,-2,2]

def four_sum(nums):
    n=len(nums)
    target=0
    if n<4:
        return []
    ans=[]
    nums.sort()

    for i in range(0,n):
        if i>0 and nums[i]==nums[i-1]:  # move foraward i
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]: # move forward j
                continue

            k=j+1
            l=n-1

            while k<l:
                total=nums[i]+nums[j]+nums[k]+nums[l]
                if total==target:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    k+=1
                    l-=1
                    while l>k and nums[k]==nums[k-1]:
                        k+=1
                    while l>k and nums[l]==nums[l+1]:
                        l-=1

                elif total < target:
                    k+=1

                else:
                    l-=1
    return ans
print(four_sum(nums))           
                              
