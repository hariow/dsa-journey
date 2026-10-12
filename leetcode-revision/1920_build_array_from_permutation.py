class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        result=[]

        for i in range(0,len(nums)):
            result.append(nums[nums[i]])
        return result

