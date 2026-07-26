# Print the Matrix in the Spiral Order

nums = [
    [ 1,  2,  3,  4,  5,  6],
    [ 7,  8,  9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

## L --> R , UP--> DOWN , R-->L , DOWN-->UP


def spiral(matrix):
    if not matrix or not matrix[0]:
        return []

    result=[]

    top=0
    bottom=len(matrix)-1
    left=0
    right=len(matrix[0])-1

    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1

        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1

    return result

print(spiral(nums))