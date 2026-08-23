## N-Queens Problem


# Brute Force

class Solution:

    def solve(self, row, board, ans, n):

        # All rows completed
        if row == n:

            if self.check_board(board, n):
                ans.append(["".join(r) for r in board])

            return

        # Try every column in this row
        for col in range(n):

            board[row][col] = "Q"

            self.solve(row + 1, board, ans, n)

            # Remove queen
            board[row][col] = "."


    def check_board(self, board, n):

        # Check columns
        for col in range(n):

            count = 0

            for row in range(n):

                if board[row][col] == "Q":
                    count += 1

            if count > 1:
                return False

        # Check diagonals
        for row in range(n):
            for col in range(n):

                if board[row][col] == "Q":

                    # Down-right
                    i = row + 1
                    j = col + 1

                    while i < n and j < n:

                        if board[i][j] == "Q":
                            return False

                        i += 1
                        j += 1

                    # Down-left
                    i = row + 1
                    j = col - 1

                    while i < n and j >= 0:

                        if board[i][j] == "Q":
                            return False

                        i += 1
                        j -= 1

        return True


    def solveNQueens(self, n):

        board = [["." for _ in range(n)] for _ in range(n)]

        ans = []

        self.solve(0, board, ans, n)

        return ans



################### Optimal Solution ######################

class Solution:
    def solve(self,col,board,ans,leftrow,upperDiagonal,lowerDiagonal,n):
        if col==n:
             
            return

        for row in range(n):

            if ( leftrow[row]==0
                and lowerDiagonal[row+col]==0
                and upperDiagonal[n-1 + col-row]==0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftrow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n - 1 + col - row] = 1

                self.solve(col+1,board,ans,leftrow,upperDiagonal,lowerDiagonal,n)

                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftrow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n - 1 + col - row] = 0





    def solveNQueen(self,n):
        ans=[]
        board=["." * n for _ in range(n)]
        leftrow = [0] * n
        upperDiagonal = [0] * (2 * n-1)
        lowerDiagonal = [0] * (2 * n-1)

        self.solve(0,board,ans,leftrow,upperDiagonal,lowerDiagonal,n)
        return ans
    
n = 4

solution = Solution()
result = solution.solveNQueen(n)

for board in result:
    for row in board:
        print(row)
    print()