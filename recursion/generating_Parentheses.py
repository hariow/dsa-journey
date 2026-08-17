#  Generating Parentheses

class Solution:
    def solve(self,index,total,brackets,result):
        if index>=len(brackets):
            if total==0:
                result.append("".join(brackets))
            return
    
        if total>len(brackets)//2:
            return

        elif total<0:
            return
        
        brackets[index]="("
        Sum=total+1

        self.solve(index+1,Sum,brackets,result)
        brackets[index]=")"
        Sum=total-1
        self.solve(index+1,Sum,brackets,result)      
        
    def parentheses(self,n):
        brackets=[""]*(n*2)
        result=[]
        self.solve(0,0,brackets,result)
        return result

s=Solution()

print(s.parentheses(3))