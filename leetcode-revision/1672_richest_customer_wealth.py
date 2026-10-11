class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        r=len(accounts)
        c=len(accounts[0])

        max_wealth=0

        for i in range(r):
            wealth=0
            for j in range(c):
                wealth += accounts[i][j]
            
            max_wealth=max(max_wealth,wealth)
        
        return max_wealth