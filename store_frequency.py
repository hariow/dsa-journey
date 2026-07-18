nums=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]

hash_map={}

n=len(nums)

for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1
    hash_map[num]=hash_map.get(num,0)

print(hash_map)