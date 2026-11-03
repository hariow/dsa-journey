## Minimum Multiplication to reach the End

from collections import deque

class Solution:
    def minSteps(self, arr, start, end):

        if start == end:
            return 0

        distance = [-1] * 1000
        distance[start] = 0

        queue = deque()
        queue.append(start)

        while queue:
            num = queue.popleft()

            for m in arr:
                new_num = (num * m) % 1000

                if distance[new_num] == -1:

                    distance[new_num] = distance[num] + 1

                    if new_num == end:
                        return distance[new_num]

                    queue.append(new_num)

        return -1