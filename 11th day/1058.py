import re
n,m=map(int,input().split())
answer=[]
error=[0]*m
a=re.escape(') (')
for i in range(m):
        answer.append(input().split())
for i in range(n):
        d=input()
        score=0
        s=re.split(a,d[1:len(d)-1])
        for j in range(m):
                c=s[j].split()
                if c[1:]==answer[j][3:]:
                        score+=int(answer[j][0])
                else:
                        error[j]+=1
        print(score)
e=max(error)
if e==0:
        print('Too simple')
        exit()
else:
        print(e,end='')
for i in range(m):
        if error[i]==e:
                print(' '+str(i+1),end='')
                
                
       

                

        
        
        
        

    
        
