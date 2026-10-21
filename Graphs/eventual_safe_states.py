from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        V=len(graph)

        adj_list=[[] for _ in range(V)]
        for node in range(V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)
        
        queue=deque()

        ## Calculate Indegrees

        indegrees=[0 for _ in range(V)]

        for node in range(len(adj_list)):
            for adjNode in adj_list[node]:
                indegrees[adjNode]+=1
        
        ## Add all the nodes with indegrees 0 in queue

        for node in range(0,V):
            if indegrees[node]==0:
                queue.append(node)
        
        result=[]

        while len(queue)!=0:
            node=queue.popleft()
            result.append(node)
            for adjNode in adj_list[node]:
                indegrees[adjNode]-=1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        result.sort()
        return result



        