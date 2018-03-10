from math import sqrt
k=int(input())
s=list(map(int,input().split()))
if k==1:
        print(s[0])
        exit()
s.sort(reverse=True)
if sqrt(k)%1==0:
        m=int(sqrt(k))
else:
        m=int(sqrt(k))+1
while k%m!=0:
        m+=1
n=int(k/m)
s=list(map(str,s))
matrix=[[0 for i in range(n)]
        for i in range(m)]
u,d,l,r=0,m-1,0,n-1
i,j,x=0,0,0
while x<k:
        while j<r and x<k:
                matrix[i][j]=s[x]
                j+=1
                x+=1
        while i<d and x<k:
                matrix[i][j]=s[x]
                i+=1
                x+=1
        while l<j and x<k:
                matrix[i][j]=s[x]
                j-=1
                x+=1
        while u<i and x<k:
                matrix[i][j]=s[x]
                i-=1
                x+=1
        u,d,l,r=u+1,d-1,l+1,r-1
        i+=1
        j+=1
        if x==k-1:
                matrix[i][j]=s[x]
                x+=1
for i in matrix:
        print(' '.join(i))
        
        
                


        
        
        

    
        
