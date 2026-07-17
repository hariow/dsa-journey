n=123

num=n
result=0
count = 0

while num > 0:
    count += 1
    num = num // 10

digits=count

num=n
while num>0:
    ld=num%10
    result +=(ld**digits)
    num=num//10

if(n==result):
    print("Armstrong Number")
else:
    print("Not Armstrong")    
