from collections import deque

## Course Schedule - I

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegrees = [ 0 for _ in range(numCourses)]

        ## O(n)

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegrees[u]+=1
        
        queue=deque()
        result=[]

        ## O(n)

        for i in range(0,numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        ## O(V + E)

        while len(queue)!=0:
            current_node = queue.popleft() # 1
            result.append(current_node)
            for adjNode in adj_list[current_node]: # 2,4
                indegrees[adjNode] -= 1
                if indegrees[adjNode] ==0:
                    queue.append(adjNode)
        
        if len(result)==numCourses:
            return True
        return False
   

## Couse Schedule - II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adj_list = [[] for _ in range(numCourses)]
        indegrees = [ 0 for _ in range(numCourses)]
        ## O(n)

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegrees[u]+=1
        
        queue=deque()
        result=[]

        ## O(n)

        for i in range(0,numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        ## O(V + E)

        while len(queue)!=0:
            current_node = queue.popleft() # 1
            result.append(current_node)
            for adjNode in adj_list[current_node]: # 2,4
                indegrees[adjNode] -= 1
                if indegrees[adjNode] ==0:
                    queue.append(adjNode)
        
        if len(result)==numCourses:
            return result
        return []
   
        