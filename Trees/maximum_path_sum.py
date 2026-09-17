## Binary Tree Maximum Path Sum

class Node:

    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right=None
        self.maxi=float('-inf')

    def solve(self,node):

        if node is None:
            return 0

        left_gain=self.solve(node.left)
        left_gain = max(0, left_gain)

        right_gain=self.solve(node.right)
        right_gain = max(0 , right_gain)

        
        self.maxi = max(self.maxi , left_gain + right_gain + node.data)

        return node.data + max(left_gain , right_gain)


root = Node(-10)

root.left = Node(9)
root.right = Node(20)

root.right.left = Node(15)
root.right.right = Node(7)

root.solve(root)

print("Maximum Path Sum:", root.maxi)


        
        