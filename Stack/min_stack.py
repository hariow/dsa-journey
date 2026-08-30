## minimum stack in 0(1)

class Solution:

    def __init__(self):
        self.items = []

    def push(self,value):
        if len(self.items)==0:
            self.items.append([value,value])
        else:
            mini=min(self.items[-1][1],value)
            self.items.append([value,mini])

    def getmin(self):
        if len(self.items)==0:
            return -1
        return self.items[-1][1]

    def top(self):
        if len(self.items)==0:
            return -1
        return self.items[-1][0]

    def pop(self):
        if len(self.items)==0:
            return -1
        return self.items.pop()[0]

stack = Solution()

stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)

print("Minimum:", stack.getmin())  # 2
print("Top:", stack.top())         # 2

print("Popped:", stack.pop())      # 2
print("Minimum:", stack.getmin())  # 3

print("Popped:", stack.pop())      # 7
print("Minimum:", stack.getmin())  # 3
    
        
