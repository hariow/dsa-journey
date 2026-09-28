from collections import deque


def updateMatrix(mat):
    row = len(mat)
    col = len(mat[0])

    visited = [[0 for _ in range(col)] for _ in range(row)]
    distance = [[0 for _ in range(col)] for _ in range(row)]

    queue = deque()

    # Add all 0s as starting points
    for r in range(row):
        for c in range(col):
            if mat[r][c] == 0:
                queue.append((r, c, 0))
                visited[r][c] = 1

    # Multi-source BFS
    while queue:
        i, j, d = queue.popleft()

        distance[i][j] = d

        # Up
        if i - 1 >= 0 and visited[i - 1][j] == 0:
            visited[i - 1][j] = 1
            queue.append((i - 1, j, d + 1))

        # Down
        if i + 1 < row and visited[i + 1][j] == 0:
            visited[i + 1][j] = 1
            queue.append((i + 1, j, d + 1))

        # Left
        if j - 1 >= 0 and visited[i][j - 1] == 0:
            visited[i][j - 1] = 1
            queue.append((i, j - 1, d + 1))

        # Right
        if j + 1 < col and visited[i][j + 1] == 0:
            visited[i][j + 1] = 1
            queue.append((i, j + 1, d + 1))

    return distance


mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

print(updateMatrix(mat))