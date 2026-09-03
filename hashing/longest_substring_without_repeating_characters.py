## longest substring without repeating characters

# Brute Force

def solve():
    chars = ['C','A','D','B','Z','A','B','C','D']
    #        i,j
    n=len(chars)
    maxi=0

    for i in range(0,n):
        my_set=set()
        for j in range(i,n):
            if chars[j] in my_set:
                break
            maxi=max(maxi,j-i+1)
            my_set.add(chars[j])

    return maxi

print(solve())


## Optimal Solution -- Sliding Window 
    
def solve_optimal():
    chars = ['C','A','D','B','Z','A','B','C','D']
    #        L             R
    n = len(chars)
    left = 0
    right = 0
    maxi = 0
    my_dict = {}

    while right < n:

        if chars[right] in my_dict:
            left = max(left, my_dict[chars[right]] + 1)

        maxi = max(maxi, right - left + 1)
        my_dict[chars[right]] = right

        right += 1

    return maxi

print(solve_optimal())


