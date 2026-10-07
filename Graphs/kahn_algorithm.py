## Kahn's Algorithm (Topological Sort)

from collections import deque


def topological_sort(V, edges):
    graph = [[] for _ in range(V)]
    indegree = [0] * V

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()

    for node in range(V):
        if indegree[node] == 0:
            queue.append(node)

    topo = []

    while queue:
        node = queue.popleft()
        topo.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo


# Example
V = 6
edges = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

print("Topological Order:", topological_sort(V, edges))