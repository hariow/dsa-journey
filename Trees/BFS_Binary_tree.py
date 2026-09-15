## Breadth First Search [Level Order Traversal]

from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def level_order(node):
        result=[]

        queue=deque([])
        queue.append(node)

        while len(queue)!=0:
            e=queue.popleft()
            result.append(e.data)

            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)

        return result
