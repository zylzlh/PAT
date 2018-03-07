s=input()
n=len(s)
leftP=[0]*n
rightT=0
count=0
for i in range(n):
        if i>0:
                leftP[i]=leftP[i-1]
        if s[i]=='P':
                leftP[i]+=1        
for i in range(n-1,-1,-1):
        if s[i]=='T':
                rightT+=1
        if s[i]=='A':
                count+=leftP[i]*rightT
num=count%1000000007
print(num)
        
                
        

    
        
