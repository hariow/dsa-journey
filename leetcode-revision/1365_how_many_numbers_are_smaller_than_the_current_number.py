class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result=[]

        for i in range(len(nums)):
            small_no = 0

            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    small_no +=1

            result.append(small_no)                    
        
        return result