class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        total=0
        n = len(mat)

        for i in range(n):
            total+=mat[i][i]
            total+=mat[i][n-1-i]

        if n%2!=0:
            total -= mat[n // 2][n // 2]

        return total