n,m=map(int,input().split())
forbiden=input().split()
count,k=0,0
d=[]
for i in range(n):
    s=input().split()
    for j in range(int(s[1])):
        if s[2+j] in forbiden:
            if s[0] not in d:
                d.append(s[0])
            d.append(s[2+j])
            k+=1
    if d:
        print('{}: {}'.format(d[0],' '.join(d[1:])))
        count+=1
    d.clear()
print(count,k)
    
    
    
            
                

        
        
        
        

    
        
