## Flood Fill 


##  DFS

from copy import deepcopy


def dfs(i,j,new_color,initial_color,vis,r,c):

    if i<0 or i>=r or j<0 or j>=c:
        return
    
    if vis[i][j]!=initial_color:
        return
    
    if vis[i][j]==new_color:
        return

    vis[i][j]=new_color

    dfs(i+1 ,j  ,new_color,initial_color,vis,r,c)
    dfs(i ,j-1  ,new_color,initial_color,vis,r,c)
    dfs(i-1 ,j  ,new_color,initial_color,vis,r,c)
    dfs(i ,j+1  ,new_color,initial_color,vis,r,c)


def flood_fill(image,sr,sc,color):

    if image[sr][sc]==color:
        return image

    vis=deepcopy(image)
    r=len(vis)
    c=len(vis[0])

    initial_color=vis[sr][sc]

    dfs(sr,sc,color,initial_color,vis,r,c)
    return vis


## Flood Fill
## BFS

from collections import deque


def flood_fill_bfs(image, sr, sc, color):

    if image[sr][sc] == color:
        return image

    rows = len(image)
    cols = len(image[0])

    initial_color = image[sr][sc]

    queue = deque()
    queue.append((sr, sc))

    # Mark starting cell immediately
    image[sr][sc] = color

    while queue:

        i, j = queue.popleft()

        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:

            new_i = i + x
            new_j = j + y

            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                continue

            if image[new_i][new_j] != initial_color:
                continue

            # Mark when adding to queue
            image[new_i][new_j] = color
            queue.append((new_i, new_j))

    return image
