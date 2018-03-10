import re
n=int(input())
score={}
for i in range(n):
        s=re.sub('-',' ',input()).split()
        try:
                if score[s[0]]:
                        score[s[0]]+=int(s[2])
        except:
                score[s[0]]=int(s[2])
res=sorted(score,key=lambda i:score[i],reverse=True)
print(res[0],score[res[0]])
                
                        

        
        
        
        

    
        
