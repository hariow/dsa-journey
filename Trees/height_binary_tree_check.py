## Check if Binary Treee is Height Balanced

class Node:

    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None


    def solve(self,node):

        if node is None:
            return 0

        LH = self.solve(node.left)

        if LH==-1:
            return -1
        
        RH = self.solve(node.right)

        if RH==-1:
            return -1
        
        if abs(LH-RH)>1:
            return -1

        return 1 + max(LH , RH)


# Example tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


x = root.solve(root)

if x == -1:
    print(False)
else:
    print(True)
    

        
        