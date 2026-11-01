## Path With Minimum Effort

import sys
import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:

        rows=len(heights)
        cols=len(heights[0])

        effort_arr=[[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        effort_arr[0][0]=0
        priority_queue=[[0,0,0]]  ## eff,i,j
        
        while len(priority_queue)!=0:
            eff,i,j=heapq.heappop(priority_queue)

            if i==rows-1 and j==cols-1:
                return eff

            for x,y in [[-1,0],[0,-1],[0,1],[1,0]]:
                new_i,new_j = i+x , j+y

                if new_i<0 or new_j<0 or new_i>=rows or new_j>=cols:
                    continue

                new_eff = max(eff,abs(heights[new_i][new_j]-heights[i][j]))

                if new_eff < effort_arr[new_i][new_j]:
                    effort_arr[new_i][new_j] = new_eff
                    heapq.heappush(priority_queue,[new_eff,new_i,new_j])