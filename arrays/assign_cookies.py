## Assign Cookies

def solve():
    greed=[2,6,8,1,4]
    s=[4,2,7,1,2,3]

    greed.sort()
    s.sort()

    n=len(greed)
    m=len(s)
    left=0
    right=0
    count=0

    while left<n and right<m:
        if greed[left]<=s[right]:
            count+=1
            left+=1
        right+=1
    return count
