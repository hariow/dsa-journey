## postfix to prefix

class Solution:

    def PostfixToPrefix(self,s):
        ## stack to store operands

        stack=[]

        ## process each character in postfix expression
        for char in s:
            ## if the character is an operand , push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                ## pop two operands from the stack

                operand2=stack.pop()
                operand1=stack.pop()

                ## combine the operans with the operator in prefix form
                new_expr=f"{char}{operand1}{operand2}"

                ## push the result back onto the stack
                stack.append(new_expr)

        ## the final element in the stack is the prefix expression

        return stack.pop()
            
