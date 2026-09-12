# Jump Game- II

# Brute Force

class Solution:

    nums=[2,3,1,4,1,1,1,2]
#         0 1 2 3 4 5 6 7
    def func(self,index,jump):
        n=len(self.nums)

        if index>=n-1:
            return jump

        min_jump=float("inf")

        for i in range(1,self.nums[index]+1):
            min_jump=min(min_jump,self.func(index+i,jump+1))

        return min_jump

solution = Solution()
print(solution.func(0, 0))


## Optimal Solution

def solve():
#        L R 
    nums=[2,3,1,4,1,1,1,2]
#         0 1 2 3 4 5 6 7

    n=len(nums)
    jump=0
    left=0
    right=0

    while right<n-1:
        farthest=0

        for i in range(left,right+1):
            farthest=max(farthest,i+nums[i])

        left=right+1
        right=farthest
        jump+=1
    return jump

print(solve())
