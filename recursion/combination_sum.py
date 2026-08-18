# Combination Sum (repetition allowed)

class Sequence:
    nums = [5, 4, 9]
    result = []
    target = 9

    def solve(self, index, total, subset, target, result):

        if total == target:
            result.append(subset.copy())
            return

        if total > target:
            return

        if index >= len(self.nums):
            return

        # Take current number
        subset.append(self.nums[index])
        self.solve(index,total + self.nums[index],subset,target,result)

        # Backtrack
        subset.pop()

        # Skip current number
        self.solve(index+1,total,subset,target,result)

    def combinationsum(self):
        self.result = []
        self.solve(0, 0, [], self.target, self.result)
        return self.result


s = Sequence()

print(s.combinationsum())