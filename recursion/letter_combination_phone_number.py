## Letter Combination of a Phone Number

class Solution:

    def solve(self,index,subset,digits,result,char_map):
        
        if index>=len(digits):
            result.append("".join(subset))
            return
                
        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.solve(index+1,subset,digits,result,char_map)
            subset.pop()


    def phone(self,digits):
             
            char_map = {
                        "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz"}
            result=[]
            self.solve(0,[],digits,result,char_map)
          
            return result
         
obj=Solution()

print(obj.phone("23"))

        