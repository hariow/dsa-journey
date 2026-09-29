## Surrounded Region


def solve(board):

    row = len(board)
    col = len(board[0])

    def dfs(i, j):
        # Out of bounds
        if i < 0 or i >= row or j < 0 or j >= col:
            return

        # Not an O
        if board[i][j] != "O":
            return

        # Mark as safe
        board[i][j] = "#"

        # Visit four directions
        dfs(i - 1, j)  # Up
        dfs(i + 1, j)  # Down
        dfs(i, j - 1)  # Left
        dfs(i, j + 1)  # Right

    # 1. Start DFS from boundary O's

    # Top and bottom rows
    for j in range(col):
        if board[0][j] == "O":
            dfs(0, j)

        if board[row - 1][j] == "O":
            dfs(row - 1, j)

    # Left and right columns
    for i in range(row):
        if board[i][0] == "O":
            dfs(i, 0)

        if board[i][col - 1] == "O":
            dfs(i, col - 1)

    # 2. Convert surrounded O's to X
    # 3. Convert safe # back to O

    for i in range(row):
        for j in range(col):

            if board[i][j] == "O":
                board[i][j] = "X"

            elif board[i][j] == "#":
                board[i][j] = "O"


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

solve(board)

for row in board:
    print(row)
