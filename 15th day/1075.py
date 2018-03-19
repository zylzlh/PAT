def link(address,head,li):
    if head in address:
        arrow=address[head]
        li.append(arrow)
        return link(address,arrow,li)
    else:
        return li
head,n,k=input().split()
address={}
data={}
for i in range(int(n)):
    s=input().split()
    address[s[0]]=s[2]
    data[s[0]]=int(s[1])
id=link(address,head,[head])
la=[]
zhen=[]
da=[]
for i in range(int(n)):
    ele=id[i]
    if data[ele]<0:
        la.append(ele)
    elif data[ele]<=int(k):
        zhen.append(ele)
    else:
        da.append(ele)
order=la+zhen+da+[-1]
for i in range(int(n)):
    print('{} {} {}'.format(order[i],data[order[i]],order[i+1]))
       
        
    
    
    
    





    
                    
                
                     
    
    
    
    
    
            
                

        
        
        
        

    
        
