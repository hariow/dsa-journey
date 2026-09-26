## Detect Cycle in Undirected Graph

## BFS

from collections import deque

class Solution:

    def IsCycle(self,V,edges):
        queue=deque()

        adj_list=[[] for _ in range(V)]

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited=[0]*V

        for i in range(0,V):
            if visited[i] == 1:
                continue

            queue.append((i,-1))
            visited[i]=1

            while len(queue)!=0:
                node,parent=queue.popleft()

                for adjNode in adj_list[node]:
                    if visited[adjNode]==0:
                        visited[adjNode]=1
                        queue.append((adjNode,node))

                    else:
                        if adjNode!=parent:
                            return True

        return False

