## Climbing Stairs


## Recursion

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)



## Recursion Memoization

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)

        def climb_stair(num,dp):
    
            if num == 1 or num == 0:
                return 1
            if dp[num] != -1:
                return dp[num]

            dp[num]=climb_stair(num-1,dp) + climb_stair(num-2,dp)
            return dp[num]
        
        return climb_stair(n,dp)



##  Tabulation 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1 or n==0:
            return 1

        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for num in range(2, n + 1):
            dp[num] = dp[num - 1] + dp[num - 2]

        return dp[n]



##  tabulation Space Optimization

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        
        prev2=1
        prev=1
        
        for i in range(2,n+1):
            curr = prev2 + prev
            prev2 = prev 
            prev = curr
        
        return prev
        
    
