class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        num_sum = [nums[0]]

        for i in range(1, len(nums)):
            num_sum.append(num_sum[i - 1] + nums[i])

        # num_sum.append(num_sum[len(nums) - 1] + nums[len(nums) - 1])
        return num_sum

