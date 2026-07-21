from math import sqrt
n = 36

Factors=[]

for i in range(1,int(sqrt(n))+1):
    if n % i == 0:
        Factors.append(i)
        if(n//i !=i):
            Factors.append(n//i)
Factors.sort()       
print(Factors)