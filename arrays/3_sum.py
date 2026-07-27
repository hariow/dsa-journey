# Three Sum Problem

#Brute Force Solution
nums=[-1,0,1,2,-1,-4]

def three_sum(nums):
    n=len(nums)
    my_set=set()

    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    my_set.add(tuple(temp))

    return[list(ans) for ans in my_set]

print(three_sum(nums))


# Better Solution

nums=[-1,0,1,2,-1,-4]

def three_sum(nums):
    n=len(nums)
    result=set()

    for i in range(0,n):
        my_set=set()

        for j in range(i+1,n):
            third=-(nums[i]+nums[j])

            if third in my_set:
                temp=[nums[i],nums[j],third]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
            
    return[list(ans) for ans in result]

print(three_sum(nums))



# Optimal Solution

nums=[-1,0,1,2,-1,-4]
#      i j         k
def three_sum(nums):
    n=len(nums)
    ans=[]
    nums.sort()

    for i in range(n-2): 
        if i!=0 and nums[i]==nums[i-1]:  ## if 2nd index also same value as first then i moves forward
            continue

        # moving two pointers

        j=i+1
        k=n-1

        while j<k:
            total_sum=nums[i]+nums[j]+nums[k]

            if total_sum<0:
                j+=1
            elif total_sum>0:
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1

                # skips the duplicate if occurred
                
                while j>k and nums[j]==nums[j-1]:
                    j+=1
                while j>k and nums[k]==nums[k+1]:
                    k-=1

    return ans

print(three_sum(nums))