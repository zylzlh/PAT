s=list(map(int,input().split()))
k=0
for i,e in enumerate(s):
        if e and i!=0:
                k=i
                break
num=str(k)
for i in range(len(s)):
        if i!=k:
                num+=str(i)*s[i]
        else:
                num+=str(i)*(s[i]-1)
print(num)
        
        
                
                
        

    
        
