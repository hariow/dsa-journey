## Count Distinct Islands

## DFS 

class Solution:
    def bfs(self,x,y,vis,grid):
        queue = [(x,y)]
        shape = [(0, 0)] 
        while queue:
            i,j = queue.pop(0)
            for dx,dy in [(0,-1),(1,0),(-1,0),(0,1)]:
                nx,ny=dx+i, dy+j
                if nx<0 or ny<0 or nx>=len(grid) or ny>=len(grid[0]):
                    continue
                if vis[nx][ny]==1:
                    continue
                if grid[nx][ny]=="W":
                    continue
                vis[nx][ny]=1
                queue.append((nx,ny))
                # record relative position most imp
                shape.append((nx-x, ny-y))
        return tuple(shape)

    def countDistinctIslands(self, grid):
        
        r, c = len(grid), len(grid[0])
        visited = [[0]*c for _ in range(r)]
        shapes = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "W" or visited[i][j] == 1:
                    continue
                shape = self.bfs(i, j, visited, grid)
                shapes.add(shape)
        return len(shapes)