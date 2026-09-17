## Top view of Binary Tree

from queue import deque

class Node:

    def __init__(self,data):
        self.data=data 
        self.left=None
        self.right= None


    def topview(self, node):

        if not node:
            return None     

        ans=[]
        queue=deque()
        result={}
        queue.append((root,0))

        while queue:
            e , line = queue.popleft()     ## e.g [5,0]->5 goes to e and 0 goes to line

            if line not in result:
                result[line]=e.data

            if e.left:
                queue.append((e.left,line-1))

            if e.right:
                queue.append((e.right,line+1))


        for line in sorted(result):
            ans.append(result[line])

        return ans







