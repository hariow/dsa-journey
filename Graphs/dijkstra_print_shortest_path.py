## Print Shortest Path Using Dijkstra | Path Reconstruction

import heapq
import sys


def shortest_path(n, m, edges):
    adj_list = [[] for _ in range(n + 1)]  ## cuz it's 1 base graph --> src=1

    for u, v, wt in edges:
        adj_list[u].append([v, wt])
        adj_list[v].append([u, wt])

    distance = [sys.maxsize for _ in range(n + 1)]
    distance[1] = 0
    
    parent = [i for i in range(0,n+1)]
    
    priority_queue=[]
    priority_queue.append([0,1])
    
    ## TC--> O(E log V)
    
    while len(priority_queue)!=0:
        dist,node=heapq.heappop(priority_queue)
        for adjNode , wt in adj_list[node]:
            dist_trav=dist+wt
            if dist_trav < distance[adjNode]:
                distance[adjNode]=dist_trav
                heapq.heappush(priority_queue,[dist_trav,adjNode])
                parent[adjNode]=node
    
    if distance[n] == sys.maxsize:
        return [-1]
    
    node=n
    path=[]
    ## TC--> O(V)
    while parent[node]!=node:
        path.append(node)
        node=parent[node]
    
    path.append(1)
    ## TC-->O(V)
    path.reverse()
    return path


n = 5
m = 6

edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]

print(shortest_path(n, m, edges))
