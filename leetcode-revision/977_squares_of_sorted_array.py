class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        left=0
        right=len(nums)-1

        result=[0]*len(nums)
        pos=len(result)-1

        while left<=right:
            if nums[left]**2 < nums[right]**2:
                result[pos]=nums[right]**2
                right-=1
                pos-=1

            elif nums[left]**2 >= nums[right]**2:
                result[pos]=nums[left]**2
                left+=1
                pos-=1
            
        return result

        