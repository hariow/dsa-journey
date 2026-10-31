## Shortes Path in Binary Matrix | BFS

import sys
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        if grid[rows-1][cols-1] == 1:
            return -1

        distance = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 1

        queue = deque()
        queue.append([1, 0, 0])

        while len(queue) != 0:
            dist, i, j = queue.popleft()

            if i == rows-1 and j == cols-1:
                return dist

            for x, y in [[1,0], [0,1], [0,-1], [-1,0],
                         [1,1], [1,-1], [-1,1], [-1,-1]]:

                nrow = i + x
                ncol = j + y

                # Check grid boundaries
                if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                    continue

                # Check whether the cell is blocked
                if grid[nrow][ncol] == 1:
                    continue

                # Calculate new distance
                new_dist = dist + 1

                # Update if a shorter distance is found
                if new_dist < distance[nrow][ncol]:
                    distance[nrow][ncol] = new_dist
                    queue.append([new_dist, nrow, ncol])

        return -1