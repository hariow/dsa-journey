## Max Consecutive One - III

# Brute Force 
def solve():

    nums=[1,1,1,0,0,0,1,1,1,1,0]

    n=len(nums)
    k=2
    maxi=0

    for i in range(0,n):
        zeros=0
        for j in range(i,n):
            if nums[j]==0:
                zeros+=1
            if zeros>k:
                break
            maxi=max(maxi,j-i+1)
    return maxi
print(solve())


## Better Solution
def solve():

    nums=[1,1,1,0,0,0,1,1,1,1,0]
#        L,R 
    n=len(nums)
    k=2
    maxi=0,left=0,right=0,zeros=0

    while right<n:
        if nums[right]==0:
            zeros+=1

        while zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        if zeros<=k:
            maxi=max(maxi,right-left+1)
        right+=1

    return maxi
print(solve())


## Optimal Solution
def solve():

    nums=[1,1,1,0,0,0,1,1,1,1,0]
#        L,R 
    n=len(nums)
    k=2
    maxi=0,left=0,right=0,zeros=0

    while right<n:
        if nums[right]==0:
            zeros+=1

        if zeros>k:          ### convert while loop --> if
            if nums[left]==0:
                zeros-=1
            left+=1
        if zeros<=k:
            maxi=max(maxi,right-left+1)
        right+=1

    return maxi
print(solve())


