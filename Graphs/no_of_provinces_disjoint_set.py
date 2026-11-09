## no of provinces using disjoint set


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
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv

        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu

        else:
            self.parent[pv] = pu
            self.rank[pu] += 1


class Solution:
    def countConnected(self, V, edges):
        ds = DisjointSet(V)

        # Merge connected vertices
        for u, v in edges:
            ds.union(u, v)

        # Count distinct components
        count = 0

        for i in range(V):
            if ds.find(i) == i:
                count += 1

        return count
