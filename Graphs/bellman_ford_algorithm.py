## Bellman Ford Algorithm

class Solution:
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        dist=[10**8 for _ in range(V)]
        dist[src]=0
        
        for _ in range(V-1):  ## N-1
            for u,v,w in edges:
                if dist[u] != 10**8:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        
        for u,v,w in edges:
            if dist[u] != 10**8:
                if dist[u] + w < dist[v]:
                    return [-1]
        return dist     
        