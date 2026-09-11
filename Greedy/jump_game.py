## Jump Game -I

def solve():

    nums=[3,2,1,0,0,2,1,5]
    #     0 1 2 3 4 5 6 7
    max_idx=0

    for i in range(0,len(nums)):
        if i > max_idx:
            return False

        max_idx = max(max_idx , i + nums[i])
    return True

print(solve())

        

