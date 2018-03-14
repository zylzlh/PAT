m=int(input())
a=list(map(int,input().split()))
a.sort()
sum=(a[0]+a[1])/2
for i in range(2,m):
    sum=sum/2+a[i]/2
print(int(sum))
        
            
        
                

        
        
        
        

    
        
