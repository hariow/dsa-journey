## Diameter of the Binary Tree

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 
        self.diameter=0

    def solve(self,node):

        if node==None:
            return 0

        left_height=self.solve(node.left)
        right_height=self.solve(node.right)

        self.diameter=max(self.diameter , left_height + right_height)

        return 1 + max(left_height,right_height)

# Creating the tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = Node(6)


# Calculate height and diameter

root.solve(root)

print("Diameter of Binary Tree:", root.diameter)
    