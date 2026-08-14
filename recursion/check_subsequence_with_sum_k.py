# Check if a Subsequence with Sum = K Exists

class Sequence:
    nums=[5,4,9]
    target=9

    def solve(self,index,total):
        if total==self.target:
            return True
        elif total>self.target:
            return False
        if index>=len(self.nums):
            return False

        pick=self.solve(index + 1, total + self.nums[index])

        if pick==True:
            return True
        
        not_pick=self.solve(index + 1, total)
        
        return not_pick
        

            

s = Sequence()
print(s.solve(0,0))
