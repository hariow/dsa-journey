## Fibonacci Tabulation(Bottom-->Up)

class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for num in range(2, n + 1):
            dp[num] = dp[num - 1] + dp[num - 2]

        return dp[n]


## Fibonacci Tabluation (Space Optimization)

class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n<=1:
            return n
        prev2=0
        prev=1
        
        for i in range(2,n+1):
            curr = prev2 + prev
            prev2 = prev 
            prev = curr
        
        return prev
    
