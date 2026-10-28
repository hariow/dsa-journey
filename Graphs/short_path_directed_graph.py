## Shortest Path in Directed Weighted Graph (DAG) | Topological Sort

class Solution:
    
    def dfs(self,node,stack,visited,adj_list):
        visited[node]=1
        for adjNode,dist in adj_list[node]:
            if visited[adjNode]==0:
                self.dfs(adjNode,stack,visited,adj_list)
                
        stack.append(node)
            
    def shortestPath(self, V: int, edges: list[list[int]]) -> list[int]:
        
        adj_list = [[] for _ in range(V)]
        
        for u , v , d in edges:
            adj_list[u].append([v,d])
        
        stack=[]
        visited=[0 for _ in range(V)]
        
        for i in range(0,V):
            if visited[i]==0:
                self.dfs(i,stack,visited,adj_list)
        
        distance=[float('inf')for _ in range(V)]
        distance[0]=0  ## distace[src]=0
        
        while len(stack)!=0:
            node=stack.pop()
            dist=distance[node]
        
            for adjNode,d in adj_list[node]:
                new_d=dist+d
                
                if new_d < distance[adjNode]:
                    distance[adjNode]=new_d
        
        for i in range(0,V):
            if distance[i]==float('inf'):
                distance[i]=-1
                
        return distance
        
        
        
        
        
        
        
        
        
        
        
        
