#  Generate All Binary Strings

class Solution:
    def solve(self,index,flag,numbers,result):
        if index>=len(numbers):
            result.append("".join(numbers))
            return
        numbers[index]="0"
        self.solve(index+1,True,numbers,result)

        if flag==True:
            numbers[index]="1"
            self.solve(index+1,False,numbers,result)
            numbers[index]="0"

    def generateBinaryStrings(self,n):
        numbers=["0"]*n
        result=[]
        self.solve(0,True,numbers,result)
        return result