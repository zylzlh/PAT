n=int(input())
a=input().split()
c=[]
for i in range(n):
    b=0
    for j in a[i]:
        b+=int(j)
    if b not in c:
        c.append(b)
c.sort()
d=list(map(str,c))
print(len(d))
print(' '.join(d))
                

        
        
        
        

    
        
