import re
f=re.escape(') (')
c=['a','b','c','d','e']
n,m=map(int,input().split())
count=[[0,0,0,0,0] for i in range(m)]
score=[]
answer=[]
for i in range(m):
    s=input().split()
    score.append(int(s[0]))
    answer.append(s[3:])
for i in range(n):
    a=input()
    k=0
    b=re.split(f,a[1:len(a)-1])
    b=[i.split() for i in b]
    for i in range(m):
        if b[i][1:]==answer[i]:
            k+=score[i]
        else:
            flag=0
            for j in b[i][1:]:
                if j not in answer[i]:
                    flag=1
                    index=c.index(j)
                    count[i][index]+=1
            if flag==0:
                k+=0.5*score[i]
    print('{:.1f}'.format(k))
if max(count)==[0,0,0,0,0]:
    print('Too simple')
else:
    times=0
    for i in range(m):
        l=max(count[i])
        if l>times:
            times=l
    for i in range(m):
        for j in range(5):
            if count[i][j]==times:
                print('{} {}-{}'.format(times,i+1,c[j]))




    
                    
                
                     
    
    
    
    
    
            
                

        
        
        
        

    
        
