# Best Time to Buy And Sell Stock

# Brute Force
prices=[1,3,2,6,1,8,4,10]
#       i j
def stk(prices):
    n=len(prices)
    max_profit=0

    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                p=prices[j]-prices[i]
                max_profit=max(max_profit,p)

        return max_profit

print(stk(prices))            


# Optimal Solution

prices=[1,3,2,6,1,8,4,10]
#       i 
def stk(prices):
    n=len(prices)
    max_profit=0
    min_price=float('inf')

    for i in range(0,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
         
    return max_profit

print(stk(prices)) 



