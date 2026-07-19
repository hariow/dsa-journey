#Head Recursion  (1 to N)

def func(i,N):
    if(i>N):
        return
    print(i)
    func(i+1,N)    

func(1,4)

 
#  Tail Recursion ( 1 to N)
 

def func(i,N):
    if(i>N):
        return
    func(i,N-1) 
    print(N)

func(1,4)


# sum of (1 to N)

def func(N):
    if(N==1):
        return 1
    return N + func(N-1)

print(func(5))

# factorial recursion

def fact(n):
    if n <= 1:
        return 1 
    return n*(fact(n-1))

print(fact(5))


# reverse an array recursion

n=[1,2,3,4,5,6,7,8,9]

def func(n,left,right):
    if(left>=right):
        return
    n[left],n[right]=n[right],n[left]
    func(n,left+1,right-1)

func(n,0,8)
print(n)