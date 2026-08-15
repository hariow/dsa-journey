# Count All Subsequences with Sum K

class Sequence:
    nums=[5,4,9]
    result=[]
    target=9

    def solve(self,index,total):
        if total==self.target:
            return 1
        elif total>self.target:
            return 0
        if index>=len(self.nums):
            return 0

        sum=total+self.nums[index]

        pick = self.solve(index+1,sum)
  
        sum=total
        not_pick = self.solve(index+1,sum)

        return pick+not_pick

            
        
s = Sequence()

print(s.solve(0, 0))
