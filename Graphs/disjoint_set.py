## Disjoint Set (Union-Find) | Path Compression + Union by Size/Rank 

class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size=[1]*(n+1)
    
    def find(self,x):
        if x == self.parent[x]: 
            return x
        
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):  ## 1,2
        pu=self.find(u)
        pv=self.find(v)
        
        if pu==pv:
            return
        
        if self.size[pu] < self.size[pv]:  ## pu -> pv
            self.parent[pu]=pv
            self.size[pv] += self.size[pu]
            
        elif self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

ds=DisjointSet(7)

ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)
 
print(ds.find(1))
print(ds.find(7))
print(ds.size)