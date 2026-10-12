class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ans=0

        for i in range(len(nums)):
            count=0
            lst_no = nums[i]

            while lst_no > 0:
                count+=1
                digit = lst_no % 10
                lst_no= lst_no // 10
            
            if count%2==0:
                ans+=1
        return ans

        