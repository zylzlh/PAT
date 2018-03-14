m,n,a,b,c=map(int,input().split())
matrix=[input().split() for i in range(m)]
instead=str(c)
while len(instead)<3:
    instead='0'+instead
for i in range(m):
    for j in range(n):
        if a<=int(matrix[i][j])<=b:
            matrix[i][j]=instead
        else:
            while len(matrix[i][j])<3:
                matrix[i][j]='0'+matrix[i][j]
for i in range(m):
    print(' '.join(matrix[i]))
            
        
                

        
        
        
        

    
        
