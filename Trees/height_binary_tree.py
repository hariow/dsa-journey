## Height of the Binary Tree

## Recursive Method   ## Optimal Sol

from collections import deque
class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 

    def solve(self,node):

        if node==None:
            return 0

        left_height=self.solve(node.left)
        right_height=self.solve(node.right)

        return 1 + max(left_height,right_height)

# Creating the tree

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)

print("Height of Binary Tree:", root.solve(root))


## Iterative Solution

def level_order(root):
    queue=deque([])
    height=0

    queue.append(root)

    while len(queue)!=0:
        level_size=len(queue)
        height+=1

        for _ in range(level_size):
            e=queue.popleft()

            if e.left is not None:
                queue.append(e.left)

            if e.right is not None:
                queue.append(e.right)

    return height

