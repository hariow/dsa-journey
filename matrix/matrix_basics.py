# Matrix Basics

# Upper Triangular Matrix

nums=[[1,2,3],[4,5,6],[7,8,9]]

row=len(nums)
col=len(nums[0])

for i in range(0,row):
    for j in range(0,col):
        if j>=i:
            print (nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()


# Lower Triangular Matrix

nums=[[1,2,3],[4,5,6],[7,8,9]]

row=len(nums)
col=len(nums[0])

for i in range(0,row):
    for j in range(0,col):
        if j<=i:
            print (nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()


# Diagonal 

nums=[[1,2,3],[4,5,6],[7,8,9]]

row=len(nums)
col=len(nums[0])

for i in range(0,row):
    for j in range(0,col):
        if j==i:
            print (nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()


# Opposite Diagonal 

nums=[[1,2,3],[4,5,6],[7,8,9]]

row=len(nums)
col=len(nums[0])

for i in range(0,row):
    for j in range(0,col):
        if i+j==row-1:
            print (nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()


# Transpose the Matrix


nums=[[1,2,3],[4,5,6],[7,8,9]]

row=len(nums)
col=len(nums[0])
result=[[0]*row for _ in range(col)]

for i in range(0,row):
    for j in range(0,col):
        result[j][i]=nums[i][j]
    
print(result)