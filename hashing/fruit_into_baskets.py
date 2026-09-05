## Fruit into Basket

# Brute Force Solution
def solve():
    nums=[3,3,3,1,2,1,1,2,3,3,4]
#         i j
    max_length=0
    n=len(nums)

    for i in range(0,n):
        my_set=set()
        for j in range(i,n):
            my_set.add(nums[j])

            if len(my_set)>2:
                break
            max_length=max(max_length,j-i+1)
    return max_length
print(solve())


## Better Solution
def solve():
    nums=[3,3,3,1,2,1,1,2,3,3,4]
#        L,R
    max_length=0
    n=len(nums)
    left=0
    right=0
    my_dict={}

    while right<n:
        my_dict[nums[right]]=my_dict.get(nums[right],0)+1

        while len(my_dict)>2:
            my_dict[nums[left]]-=1
            
            if my_dict[nums[left]]==0:
                del my_dict[nums[left]]
            left+=1

        if len(my_dict)<=2:
            max_length=max(max_length,right-left+1)
        right+=1
    return max_length
print(solve())


## Optimal Solution
def solve():
    nums=[3,3,3,1,2,1,1,2,3,3,4]
#        L,R
    max_length=0
    n=len(nums)
    left=0
    right=0
    my_dict={}

    while right<n:
        my_dict[nums[right]]=my_dict.get(nums[right],0)+1

        if len(my_dict)>2:            ## while loop --> if
            my_dict[nums[left]]-=1

            if my_dict[nums[left]]==0:
                del my_dict[nums[left]]
            left+=1

        if len(my_dict)<=2:
            max_length=max(max_length,right-left+1)
        right+=1
    return max_length
print(solve())

