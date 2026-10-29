## Dijkstra’s Algorithm Using Priority Queue


## GFG 
import heapq

class Solution:
    def dijkstra(self, adj: list[list[list[int]]], src: int) -> list[int]:
        V = len(adj)

        distance = [float("inf")] * V
        distance[src] = 0

        priority_queue = [(0, src)]

        while priority_queue:
            curr_dist, node = heapq.heappop(priority_queue)

            if curr_dist > distance[node]:
                continue

            for adjNode, weight in adj[node]:
                new_dist = curr_dist + weight

                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(priority_queue, (new_dist, adjNode))

        return distance