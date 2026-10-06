## Topological Sort Using DFS   

class Solution:
    
    def dfs(self,current_node,visited,stack,adj_list):
        visited[current_node] = 1
        
        for adjNode in adj_list[current_node]:
            if visited[adjNode]==0:
                self.dfs(adjNode,visited,stack,adj_list)
                
        stack.append(current_node)
        
            
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        
        adj_list=[[] for _ in range(V)]
        
        for u,v in edges:
            adj_list[u].append(v)
        
        stack=[]
        visited=[0 for _ in range(V)]
        
        for i in range(0,V):
            if visited[i]==0:
                self.dfs(i,visited,stack,adj_list)
        
        return stack[::-1]