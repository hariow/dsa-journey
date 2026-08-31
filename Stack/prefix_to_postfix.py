## prefix to postfix

class Solution:

    def PrefixToPostfix(self,s):
        # stack to store operands
        stack=[]

        ## traverse the prefix expression from right to left using index

        n=len(s)

        for i in range(n-1,-1,-1):   ## reverse iteration using index
            char =s[i]

            ## if the character is an operand , push it to the stack

            if char.isalnum():
                stack.append(char)
            else:
                ## pop two operands from the stack
                operand1=stack.pop()
                operand2=stack.pop()

                ## combine the operand with the operator in postfix form
                new_expr=operand1+operand2+char

                ## push the result back onto the stack

                stack.append(new_expr)

        return stack.pop()

