n=int(input())
partner={}
a=[]
for i in range(n):
    s=input().split()
    partner[s[0]]=s[1]
    partner[s[1]]=s[0]
    a.append(s[0])
    a.append(s[1])
m=int(input())
candidate=input().split()
singledog=[]
for i in candidate:
    if i not in a:
        singledog.append(i)
    else:
        if partner[i] not in candidate:
            singledog.append(i)
singledog.sort()
print(len(singledog))
if len(singledog):
    print(' '.join(singledog))
        
                

        
        
        
        

    
        
