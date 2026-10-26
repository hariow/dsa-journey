## Eventual Safe State Using DFS

class Solution(object):
    def dfs(self,current_node,adj_list,vis,path_vis,is_safe):
        vis[current_node] = 1
        path_vis[current_node] = 1

        for adjNode in adj_list[current_node]:
            if vis[adjNode] == 0:
                ans = self.dfs(adjNode,adj_list,vis,path_vis,is_safe)

                if ans == False:
                    return False
            
            elif path_vis[adjNode] == 1:
                return False    
        
        is_safe[current_node]=1
        path_vis[current_node]=0
        return True


    def eventualSafeNodes(self, graph):
        V=len(graph)
        vis = [0 for _ in range(V)]
        path_vis = [0 for _ in range(V)]
        is_safe = [0 for _ in range(V)]  ## [0,0,0,0,1,1,1,0]

        for i in range(0,V):
            if vis[i]==0:
                self.dfs(i,graph,vis,path_vis,is_safe)
        
        result=[]

        for i in range(V):
            if is_safe[i]==1:
                result.append(i)
        
        return result
   