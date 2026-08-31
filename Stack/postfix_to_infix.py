## postfix to infix 

class Solution:

    def PosttoInfix(self,s):
        # stack to store operands
        stack=[]

        for char in s:
            # if character is an operand, push it to the stack
            if char.isalnum():  ## alnum is alphanumeric in python
                stack.append(char)
            else:
                ## Pop two operands

                operand1=stack.pop() ## pop last most element
                operand2=stack.pop() ## pop last second element

                ## combine operands with the operator

                new_expr=f"({operand2}{char}{operand1})"

                ## Push the result back onto the stack
                stack.append(new_expr)

        ## the final element in the stack is the infix expression

        return stack.pop()
                
