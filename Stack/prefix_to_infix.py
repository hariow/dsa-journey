## prefix to infix

class Solution:

    def PrefixtoInfix(self,s):

        ## stack to store operands
        stack=[]

        for char in s[::-1]:
            ## if character is an operand , push it to the stack

            if char.isalnum():
                stack.append(char)

            else:
                ## pop two operands but with reversed order

                operand1=stack.pop()
                operand2=stack.pop()

                ## combine operands with the operator

                new_expr=f"({operand1}{char}{operand2})"

                ## push the result back onto the stack

                stack.append(new_expr)

        ## The final element in the stack is the infix expression

        return stack.pop()