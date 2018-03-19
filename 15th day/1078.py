def de(s):
    count=len(s)
    out=''
    i=0
    k=1
    while i<count:
        if '0'<=s[i]<='9':
            while True:
                if '0'<=s[i+k]<='9':
                    k+=1
                else:
                    break
            out=out+int(s[i:i+k])*s[i+k]
            i+=k+1
        else:
            out=out+s[i]
            i+=1
    return out
def co(s):
    count=len(s)
    i=0
    out=''
    while i<count:
        k=1
        while i<=count-2 and s[i]==s[i+1]:
                i+=1
                k+=1
        if k>1:
            out=out+str(k)+s[i]
        else:
            out=out+s[i]
        i+=1
    return out
n=input()
s=input()
if n=='C':
    out=co(s)
else:
    out=de(s)
print(out)
    
    
    





    
                    
                
                     
    
    
    
    
    
            
                

        
        
        
        

    
        
