# Print the following pattern for the given number of rows.
# Pattern for N = 4
#            1
#          232
#        34543
#      4567654


n= int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(' ',end='')
        s=s+1
    num=1
    p=i
    while num<=i:
        print(p,end='')
        num=num+1
        p=p+1
    p=i-1
    
    while p>=1:
        print(p+i-1,end='')
        p=p-1
        
        
    print()
    i=i+1