n = ['N', 'I', 'T', 'I', 'N']

left=0
right=len(n)-1

while(left<right):
    if(n[left]!=n[right]):
        print("Not Palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")
        
   


# Recursion Palindrome

n = ['A','A','B','C','D','A']

def func(n,left,right):
    if(left>=right):
        return True
    if(n[left]!=n[right]):
        return False

    return func(n,left+1,right-1)

print(func(n, 0, len(n) - 1))

