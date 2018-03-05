n,p=map(int,input().split())
s=list(map(int,input().split()))
s.sort()
num=0
for i in range(n):
        M=s[i]*p
        next_=i+num
        if next_>=n:
                break
        for j in range(next_,n):
                if s[j]<=M:
                        num+=1
                else:
                        break
print(num)
        
                
        

    
        
