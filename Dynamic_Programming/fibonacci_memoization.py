## Fibonacci Memorization (Top-->Down)

class Solution:
    def nthFibonacci(self, n: int) -> int:
        dp=[-1]*(n+1)
        
        def fib(num,dp):
            if num<=1:
                return num
                
            if dp[num]!=-1:
                return dp[num]
                
            dp[num]=fib(num-1,dp)+fib(num-2,dp)
            
            return dp[num]
        
        return fib(n,dp)
        
        
