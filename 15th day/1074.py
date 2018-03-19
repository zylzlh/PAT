a=[10,1,2,3,4,5,6,7,8,9]
n=input()
b=input()
c=input()
if int(b)==0 and int(c)==0:
    print(0)
    exit()
k=min(len(b),len(c))
j=max(len(b),len(c))
if len(b)==k:
    b=(j-k)*'0'+b
else:
    c=(j-k)*'0'+c
jin=0
i=-1
out=''
while j:
    d=int(b[i])+int(c[i])+jin
    jinzhi=a[int(n[i])]
    jin=d//jinzhi
    if jinzhi<=d:
        yu=d%jinzhi
    else:
        yu=d
    out=str(yu)+out
    i-=1
    j-=1
while jin:
    jinzhi=a[int(n[i])]
    if jin>=jinzhi:
        yu=jin%jinzhi
    else:
        yu=jin
    jin//=jinzhi
    out=str(yu)+out
    i-=1
out=list(out)
flag=0
for i in out:
    if i!='0':
        flag=1
    if i=='0'and flag==0:
        out.remove('0')
print(''.join(out))
    
        
        
    
    
    
    





    
                    
                
                     
    
    
    
    
    
            
                

        
        
        
        

    
        
