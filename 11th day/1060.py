n=int(input())
s=list(map(int,input().split()))
E=0
s.sort(reverse=True)
for i in range(n):
        if s[i]>i+1:
                E+=1
print(E)
                

        
        
        
        

    
        
