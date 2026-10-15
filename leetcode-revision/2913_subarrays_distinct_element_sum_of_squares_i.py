class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j+1]
                dis_count = len(set(subarray))
                total += dis_count ** 2

        return total