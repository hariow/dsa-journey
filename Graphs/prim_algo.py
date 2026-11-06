## Prim's Algorithm Minimum Spanning Tree

from typing import List
import heapq


class Solution:
    def primMST(self, adj: list[list[list[int]]]) -> int:
        mst=[]
        Sum=0
        vis=[0 for _ in range(len(adj))]
        priority_queue=[]
        priority_queue.append([0,0,-1])  ## [wt,node,parent]
        
        while priority_queue:
            wt,node,parent=heapq.heappop(priority_queue)
            if vis[node]==0:
                vis[node]=1
                if parent != -1:
                    Sum += wt
                    mst.append([parent,node])
                    
                for adjNode, wtt in adj[node]:
                    if vis[adjNode] == 0:
                        heapq.heappush(priority_queue,[wtt,adjNode,node])
        
        return Sum
       