# Minimum Bit Flips to Convert Number

def flip(start,goal):
    ans = start^goal 
    count=0

    for i in range(0,32):
        if ans&(1<<i)!=0:
            count+=1

    return count

print(flip(10,7))
