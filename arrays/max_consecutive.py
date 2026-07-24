# Max Consecutive Ones

nums=[1,2,3,1,1,1,1,1,0,2,1,1,1,1,1,1,1]

n=len(nums)

def mx_csc(nums,n):
    count=0
    maximum=0
    for i in range(0,n):
        if nums[i]==1:
            count+=1
            if count>maximum:
                maximum=count
        else:
            count=0   

    return maximum

print(mx_csc(nums,n))