## Minimum Spanning Tree Using Kruskal’s Algorithm


from typing import List


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True


class Solution:
    def primMST(self, adj: List[List[List[int]]]) -> int:
        V = len(adj)

        edges = []
        seen = set()

        for u in range(V):
            for neighbour in adj[u]:
                v, w = neighbour

                if (min(u, v), max(u, v)) not in seen:
                    seen.add((min(u, v), max(u, v)))
                    edges.append((w, u, v))

        edges.sort()

        dsu = DisjointSet(V)
        mst_weight = 0
        count = 0

        for w, u, v in edges:
            if dsu.union(u, v):
                mst_weight += w
                count += 1

            if count == V - 1:
                break

        return mst_weight
             