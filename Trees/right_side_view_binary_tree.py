## Right Side View of the Binary Tree

# Brute Force

from queue import deque

class Node:

    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right= None


    def rightview(self, node):

        if not node:
            return None     

        result=[]
        queue=deque()
        queue.append(node)

        while len(queue)!=0:
            level_size=len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i==level_size-1:
                    result.append(node.data)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result


## Optimal Solution


def reverse_postorder(node,level,ans):

    if node is None:
        return

    if len(ans) == level:
        ans.append(node.data)

    if node.right:
        reverse_postorder(node.right , level+1,ans)

    if node.left:
        reverse_postorder(node.left , level+1, ans)

ans=[]
reverse_postorder(root,0,ans)
 
return ans


    

