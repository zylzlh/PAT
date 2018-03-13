from math import sqrt
n=int(input())
r=[list(map(int,input().split())) for i in range(n)]
s=[r[i][0]**2+r[i][1]**2 for i in range(n)]
R=max(s)
print('{:.2f}'.format(sqrt(R)))
                

        
        
        
        

    
        
