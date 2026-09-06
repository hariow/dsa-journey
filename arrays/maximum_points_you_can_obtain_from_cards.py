## Maximum Points Can Obtain From Cards

def solve():
    nums=[1,2,3,4,5,6,1]
    #     0 1 2 3 4 5 right idx
    k=3
    n=len(nums)

    if n==k:
        return sum(nums)

    left_sum=0
    right_sum=0
    maxi=0

    for i in range(0,k):
        left_sum+=nums[i]

    maxi=left_sum

    right_idx=n-1

    for i in range(k-1,-1,-1):
        left_sum-=nums[i]
        right_sum+=nums[right_idx]
        maxi=max(maxi , left_sum + right_sum)

        right_idx-=1
    return maxi

print(solve())



