##  Implement Stack using Queue

from collections import deque

class StackusingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue)==0:
            return "Stack is Empty"
        return self.queue.popleft()
    
    def peek(self):
        if len(self.queue)==0:
            return "Stack is Empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)
    
        