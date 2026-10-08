## Detect cycle in Directed Graph

class Solution:

    def dfs(self, node, visited, path_visited, adj):
        visited[node] = 1
        path_visited[node] = 1

        for neighbor in adj[node]:

            if visited[neighbor] == 0:
                if self.dfs(neighbor, visited, path_visited, adj):
                    return True

            elif path_visited[neighbor] == 1:
                return True

        path_visited[node] = 0
        return False

    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        visited = [0] * V
        path_visited = [0] * V

        for node in range(V):
            if visited[node] == 0:
                if self.dfs(node, visited, path_visited, adj):
                    return True

        return False