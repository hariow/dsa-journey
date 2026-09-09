## Minimum Number of Coins

def solve():

    coins=[1,2,5,10,20,50,100,200,500,2000]
    n=len(coins)
    k=43
    result=[]

    for i in range(n-1,-1,-1):
        while k>=coins[i]:
            result.append(coins[i])
            k-=coins[i]

    return result
        

        
