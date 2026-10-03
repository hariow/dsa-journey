## Number of Islands

from collections import deque


class Solution:

    # BFS
    def bfs(self, i, j, visited, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1

        while queue:

            x, y = queue.popleft()

            for xx, yy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

                new_i = x + xx
                new_j = y + yy

                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue

                if grid[new_i][new_j] == "0":
                    continue

                if visited[new_i][new_j] == 1:
                    continue

                visited[new_i][new_j] = 1
                queue.append((new_i, new_j))


    # DFS
    def dfs(self, i, j, visited, grid):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return

        if grid[i][j] == "0":
            return

        if visited[i][j] == 1:
            return

        visited[i][j] = 1

        self.dfs(i + 1, j, visited, grid)
        self.dfs(i - 1, j, visited, grid)
        self.dfs(i, j + 1, visited, grid)
        self.dfs(i, j - 1, visited, grid) 


    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and visited[r][c] == 0:

                    count += 1

                    self.bfs(r, c, visited, grid)

        return count