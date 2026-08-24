## Rate in a Maze        --->> order-->> DLRU

class Solution:
    def solve_maze(self,maze,row,col,n,path,visited,answer):

        if row==n-1 and col==n-1:  ## reached 
            answer.append(path)
            return

        ## down
        if row + 1 < n and maze[row+1][col] == 1 and visited[row + 1][col] == 0:
            visited[row+1][col] = 1
            self.solve_maze(maze,row+1,col,n,path+"D",visited,answer)
            visited[row+1][col] = 0

        ## left
        if col - 1 >=0 and maze[row][col-1] == 1 and visited[row][col-1] == 0:
            visited[row][col-1] = 1
            self.solve_maze(maze,row,col-1,n,path+"L",visited,answer)
            visited[row][col-1] = 0

        ## right

        if col + 1 < n  and maze[row][col+1] == 1 and visited[row][col+1] == 0:
            visited[row][col+1] = 1
            self.solve_maze(maze,row,col+1,n,path+"R",visited,answer)
            visited[row][col+1] = 0

        ## up
        if row - 1 >= 0 and maze[row - 1][col] == 1 and visited[row - 1][col] == 0:
            visited[row - 1][col] = 1
            self.solve_maze(maze, row - 1, col, n, path + "U", visited, answer)
            visited[row - 1][col] = 0



    def rat_in_maze(self,maze):
        n=len(maze)

        answer=[]

            ## Create visited matrix

        visited = [[0 for _ in range(n)]for _ in range(n)]

            ## if starting cell is blocked

        if maze[0][0] == 0:
            return answer

        visited[0][0] = 1

        self.solve_maze(maze,0,0,n,"",visited,answer)
        return answer

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

solution=Solution()
print(solution.rat_in_maze(maze))
        

