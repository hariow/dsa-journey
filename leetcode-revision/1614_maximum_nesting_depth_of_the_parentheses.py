class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        count=0

        for i in range(len(s)):
            
            if s[i]=="(":
                count+=1
                ans = max(count,ans)

            elif s[i]==")":
                count-=1
            
        return ans