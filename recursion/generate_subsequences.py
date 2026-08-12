# Advanced Recursion | Generate All Subsequences Using Recursion

class Sequence:
    nums=[5,7,9]
    result=[]

    def func(self,index,subset):
        if index >= len(self.nums):
            self.result.append(subset.copy())
            return
        
        subset.append(self.nums[index])
        self.func(index+1,subset)
        subset.pop()
        self.func(index+1,subset)



s = Sequence()
s.func(0, [])

print(s.result)
