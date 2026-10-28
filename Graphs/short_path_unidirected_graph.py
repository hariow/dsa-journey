##  Shortest Path in Undirected Graph with Unit Distance | BFS


## in gfg --> Shortest Path in Unweighted Graph

from collections import deque

class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        distance = [-1] * V
        queue = deque()

        distance[src] = 0
        queue.append(src)

        while queue:
            node = queue.popleft()

            if node == dest:
                return distance[node]

            for adjNode in adj[node]:
                if distance[adjNode] == -1:
                    distance[adjNode] = distance[node] + 1
                    queue.append(adjNode)

        return -1