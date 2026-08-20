# Subset Sums 1

# Brute Force

class Solution:
    def solve(self, nums, index, subset, result):
        # Base case: processed all elements
        if index >= len(nums):
            result.append(sum(subset))  # Calculate sum of current subset
            return
        
        # Choice 1: Include current element
        subset.append(nums[index])
        self.solve(nums, index + 1, subset, result)
        
        # Backtrack: Remove current element  
        subset.pop()
        
        # Choice 2: Exclude current element
        self.solve(nums, index + 1, subset, result)

    def subsetSums(self, arr):
        result = []
        self.solve(arr, 0, [], result)
        result.sort()  # Sort as required by problem
        return result


## Optimal Solution

class Solution:

    def solve(self, index, total, result):

        if index >= len(self.nums):
            result.append(total)
            return

        # Pick
        Sum = total + self.nums[index]
        self.solve(index + 1, Sum, result)

        # Not Pick
        self.solve(index + 1, total, result)

    def subsetSums(self, arr):
        self.nums = arr
        result = []

        self.solve(0, 0, result)

        result.sort()
        return result


