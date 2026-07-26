# Set Matrix Zero

# Brute Force Solution

nums = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
def markinfinity(matrix,row,col):
    r = len(matrix)
    c = len(matrix[0])

    for i in range(0,r):
        if matrix[i][col]!=0:
            matrix[i][col]=float('inf')

    for j in range(0,c):
        if matrix[row][j]!=0:
            matrix[row][j]=float('inf')

def setZeroes(matrix):
    r = len(matrix)
    c = len(matrix[0])

    for i in range (0,r):
        for j in range(0,c):
            if matrix[i][j]==0:
                markinfinity(matrix,i,j)

    for i in range (0,r):
            for j in range(0,c):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0

setZeroes(nums)
print(nums)


# Optimal Solution


nums = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

r=len(nums)
c=len(nums[0])

row_track=[0 for _ in range(r)]
col_track=[0 for _ in range(c)]

for i in range(0,r):
    for j in range(0,c):
        if nums[i][j]==0:
            row_track[i]=-1
            col_track[j]=-1

for i in range(0,r):
    for j in range(0,c):
        if row_track[i]==-1 or col_track[j]==-1:
            nums[i][j]=0

print(nums)