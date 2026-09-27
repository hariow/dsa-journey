## Detect Cycle in Undirected Graph


## DFS

from collections import deque

class Solution:
    def dfs(self, node, parent, visited, adj_list):
        visited[node] = 1

        for adjNode in adj_list[node]:
            if visited[adjNode] == 0:
                ans = self.dfs(adjNode, node, visited, adj_list)

                if ans == True:
                    return True

            elif visited[adjNode] == 1 and adjNode != parent:
                return True

        return False

    def isCycle(self, V, edges):
        adj_list = [[] for _ in range(V)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0] * V

        for i in range(0, V):
            if visited[i] == 1:
                continue

            if self.dfs(i, -1, visited, adj_list) == True:
                return True

        return False