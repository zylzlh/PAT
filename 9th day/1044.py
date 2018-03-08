n=int(input())
s=list(map(int,input().split()))
leftL=[0]
rightS=[0]*n
for i in range(n):
        if i==0:
                leftL[i]=0
        else:
                leftL.append(max(leftL[i-1],s[i-1]))
for i in range(n-1,-1,-1):
        if i==n-1:
                rightS[i]=float('inf')
        else:
                rightS[i]=min(rightS[i+1],s[i+1])
count=0
zhuyuan=[]
for i in range(n):
        if leftL[i]<s[i]<rightS[i]:
                count+=1
                zhuyuan.append(str(s[i]))
print(count)
print(' '.join(zhuyuan))
                        
        
        

    
        
