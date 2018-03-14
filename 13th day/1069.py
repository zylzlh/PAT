m,n,s=map(int,input().split())
a=[]
d=[]
flag=0
for i in range(1,m+1):
    a.append(input())
    if (i-s)%n==0 and i>=s:
        if a[i-1] not in d:
            print(a[i-1])
            d.append(a[i-1])
            flag=1
        else:
            s+=1
if flag==0:
    print('Keep going...')

        
            
        
                

        
        
        
        

    
        
