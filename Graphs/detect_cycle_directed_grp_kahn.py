## Detect Cycle in Directed Graph using Kahn’s Algorithm


from collections import deque

class Solution:
    def isCyclic(self, V, edges):
        adj_list = [[] for _ in range(V)]
        indegrees = [0 for _ in range(V)]

        # Build adjacency list and calculate indegrees
        for u, v in edges:
            adj_list[u].append(v)
            indegrees[v] += 1

        # Add all nodes with indegree 0
        queue = deque()

        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        # Kahn's Algorithm
        count = 0

        while queue:
            current_node = queue.popleft()
            count += 1

            for adj_node in adj_list[current_node]:
                indegrees[adj_node] -= 1

                if indegrees[adj_node] == 0:
                    queue.append(adj_node)

        # If some nodes remain unprocessed, a cycle exists
        return count != V

