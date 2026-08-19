#Combination Sum II

# Brute Force 

class Solution:

    def solve(self, index , total , target , subset, nums, result):
        if total == target:
            subset.sort()
            subset = tuple(subset)
            result.add(subset)
            return
        elif total>target:
            return
        if index>= len(nums):
            return
        sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index+1, sum, target, subset, nums, result)
        sum = total
        subset.pop()
        self.solve(index+1, sum, target, subset, nums, result)

    def combutionsum2(self, nums, target):
        result = set()
        self.solve(0, 0, target, [], nums, result)
        return result
obj = Solution()
print(obj.combutionsum2([1,1,2,1,2], 4))


## Optimal Solution

class  Solution:

    def backtracking(self, index, total, subset, nums, result):
        if total==0:
            result.append(subset.copy())
            return

        if total<0:
            return

        if index>=len(nums):
            return

        for i in range(index,len(nums)):
            if i > index and nums[i]==nums[i-1]:
                continue

            subset.append(nums[i])
            sum=total-nums[i]

            self.backtracking(i+1,sum,subset,nums,result)
            subset.pop()

    def combinationSum2(self, nums, target):
        nums.sort()
        result = []
        self.backtracking(0, target, [], nums, result)
        return result

obj=Solution()

print(obj.combinationSum2([1, 1, 2, 1, 2], 4))
