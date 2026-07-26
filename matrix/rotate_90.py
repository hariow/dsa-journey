# Rotate Matrix By 90 Degree

# Brute Force Solution

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def rotate(matrix):
    r = len(matrix)
    c = len(matrix[0])

    result=[[0 for _ in range(r)]for _ in range (r)] # (no. of zeros)*(no. of times) 

    for i in range(0,r):
        for j in range(0,c):
            result[j][(r-1)-i]=nums[i][j]
    return result

print(rotate(nums))


# Optimal Solution

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def rotate(matrix):
    n= len(matrix)    # 3

    for i in range(0,n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]  ## Transpose the Matrix

    for i in range(0,n):
        matrix[i].reverse() ## Reverse the Matrix

    return matrix

print(rotate(nums))