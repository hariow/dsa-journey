# Rearrange Array Elements by Sign

#Brute Force
nums=[1,2,3,-4,-5,-6]

def sign(nums):
    n=len(nums)

    pos=[]
    neg=[]

    for i in range(0,n):
        if nums[i]>=0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    for i in range(0,len(pos)):   # made an formula that puts pos and neg
        nums[2*i]=pos[i]
        nums[(2*i)+1]=neg[i]

    return nums

print(sign(nums))


# Optimal Solution

nums=[1,2,3,-4,-5,-6]

def sign(nums):
    n=len(nums)
    result=[0]*n
    pos_ind=0
    neg_ind=1

    for i in range(0,n):
        if nums[i]>=0:
            result[pos_ind]=nums[i]
            pos_ind+=2
        else:
            result[neg_ind]=nums[i]
            neg_ind+=2

    return result

print(sign(nums))
