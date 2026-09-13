## Minimum Platform Required


# Brute Force

def solve():

    arr=[900,940,950,1100,1500,1800]
    dep=[910,1200,1120,1130,1900,2000]

    ans=1

    for i in range(len(arr)):
        count=1
        for j in range(len(arr)):
            if(i!=j):
                if arr[i]>=arr[j] and arr[i]<=dep[j]:
                    count+=1

        ans=max(ans,count)

    return ans

print(solve())


# Optimal Solution

class Solution:
    def minimumPlatform(self, arr, dep):

        arr=[900,940,950,1100,1500,1800]
        #         i
        dep=[910,1200,1120,1130,1900,2000]
        #     j

        arr.sort()
        dep.sort()

        ans = 1
        count = 1
        i = 1
        j = 0
        
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:  # one more platform needed
                count += 1
                i += 1
            else:  # one platform can be reduced
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans
    

    
