## Smallest City with Threshold Neighbors

## Floyd Warshall


import sys
from typing import List

class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        INF = sys.maxsize
        # build adjacency matrix
        dist = [[INF] * n for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for i in range(n):
            dist[i][i] = 0

        # Floyd-Warshall triple loop
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != INF and dist[via][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])

        # count reachable neighbors
        min_cnt, city = n + 1, -1
        for i in range(n):
            cnt = sum(dist[i][j] <= distanceThreshold for j in range(n))
            # ≥ keeps the larger index on ties
            if cnt <= min_cnt:
                min_cnt, city = cnt, i
        return city
    
    

## Dijkstra from every City


import sys, heapq
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        INF = sys.maxsize
        def dijkstra(src: int) -> List[int]:
            dist = [INF] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        min_cnt, city = n + 1, -1
        for i in range(n):
            row = dijkstra(i)
            cnt = sum(d <= distanceThreshold for d in row)
            if cnt <= min_cnt:            # "<=" keeps larger index on tie
                min_cnt, city = cnt, i
        return city