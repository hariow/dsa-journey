##  Advanced Recursion | Generate Subsequences with Sum K 
class Sequence:
    nums=[5,4,9]
    result=[]
    target=9

    def solve(self,index,total,subset):
        if total==self.target:
            self.result.append(subset.copy())
            return
        elif total>self.target:
            return
        if index>=len(self.nums):
            return

        subset.append(self.nums[index])
        sum=total+self.nums[index]

        self.solve(index+1,sum,subset)
        e=subset.pop()
        sum=sum-e
        self.solve(index+1,sum,subset)
        

            
        

s = Sequence()
s.func(0, [])

print(s.result)
