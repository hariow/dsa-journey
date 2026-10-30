## Dijkstra’s Algorithm Using Set


## time complexity is higher than the priority queue so use priority queue

import sys


class Solution:
    def dijkstra(self, V, edges, src):
        adj_list = [[] for _ in range(V)]

        for u, v, d in edges:
            adj_list[u].append((v, d))
            adj_list[v].append((u, d))

        distance = [sys.maxsize for _ in range(V)]
        distance[src] = 0

        my_set = set()
        my_set.add((0, src))

        while len(my_set) != 0:
            dist, node = min(my_set)
            my_set.discard((dist, node))

            for adjNode, weight in adj_list[node]:
                dist_trav = dist + weight

                if dist_trav < distance[adjNode]:
                    if distance[adjNode] != sys.maxsize:
                        my_set.discard((distance[adjNode], adjNode))

                    distance[adjNode] = dist_trav
                    my_set.add((dist_trav, adjNode))

        return distance
