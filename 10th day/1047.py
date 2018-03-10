s=['0','1','2','3','4','5','6','7','8','9','J','Q','K']
a,b=input().split()
c=len(b)-len(a)
if c<0:
        b=abs(c)*'0'+b
else:
        a=c*'0'+a
code=''
k=1
for i in range(len(b)-1,-1,-1):
        if k%2!=0:
                n=(int(b[i])+int(a[i]))%13
        else:
                n=int(b[i])-int(a[i])
                if n<0:
                        n+=10
        code=s[n]+code
        k+=1
print(code)
        
        
        
        

    
        
