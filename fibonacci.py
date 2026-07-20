## factorial using recursion 

def func(n):
    if(n==1 or n==0):
        return n
    else:
        return func(n-1)+func(n-2)
    

print(func(4))
  