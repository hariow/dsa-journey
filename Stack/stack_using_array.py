class Stack:

    def __init__(self):
        self.items =[]    ## creating list

    def is_empty(self):               
        return len(self.items) == 0   ## return if list empty

    def push(self,item):     
        self.items.append(item)      ## append

    def pop(self):
        if len(self.items)==0:     ## stack empty no pop
            return "Cannot pop , stack is empty"
        x=self.items.pop()      ## removes top most element
        return x

    def top(self):
        if len(self.items)==0:     ## stack empty no top
            return "Cannot top , stack is empty"
        return self.items[-1]     ## returns top most element

    def size(self):
        return len(self.items)      ## returns size of the element

stack=Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print(f"Stack content = {stack.items}")
print(f"Popped item = {stack.pop()}")
print(f"Stack Content = {stack.items}")
print(f"Top item after pop = {stack.top()}")
print(f"Stack is empty = {stack.is_empty()}")
