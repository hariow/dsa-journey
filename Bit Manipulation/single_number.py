# Find the Single Number

# Brute Force
arr=[1,2,3,2,3]

def find_single(arr):

    hash_map={}

    for num in arr:
        hash_map[num]=hash_map.get(num,0)+1

    for key in hash_map:
        if hash_map[key]==1:
            return key

print(find_single(arr))


## Optimal Solution

arr=[1,2,3,2,3,4,5,4,5]

def find_single(arr):

    ans=0

    for num in arr:
        ans=ans^num
    return ans

print(find_single(arr))

        