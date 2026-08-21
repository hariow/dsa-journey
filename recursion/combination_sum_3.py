## Combination Sum III


class Solution:

    def backtracking(self, index, total, subset, nums, result, k):

        if total == 0 and k == 0:
            result.append(subset.copy())
            return

        if total < 0 or k == 0:
            return

        for i in range(index, len(nums)):

            subset.append(nums[i])

            new_total = total - nums[i]
            new_k = k - 1

            self.backtracking(i + 1,new_total,subset,nums,result,new_k)

            subset.pop()

    def combinationSum3(self, nums, target, k):

        result = []

        self.backtracking(0, target, [], nums, result, k)

        return result


obj = Solution()

print(obj.combinationSum3([1,2,3,4,5,6,7,8,9], 9, 3))


## Leetcode Solution

class Solution:
    def solve(self,last,total,subset,k,n,result):

        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        
        if total>n or len(subset)>k:
            return
        
        for i in range(last,10):
            Sum=total+i
            subset.append(i)

            self.solve(i+1,Sum,subset,k,n,result)
            subset.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.solve(1,0,[],k,n,result)
        return result

        