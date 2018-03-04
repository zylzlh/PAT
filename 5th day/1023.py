import re
s=input()
a,b=re.split('E',s)
if a[0]=='+':
        c=''
else:
        c='-'
if int(b)<0:
        print(c+'0.'+'0'*(abs(int(b))-1)+a[1]+a[3:])
elif int(b)==0:
        print(c+a[1:])
elif int(b)<len(a[3:]):
        print(c+a[1]+a[3:int(b)+3]+'.'+a[int(b)+3:])
else:
        print(c+a[1]+a[3:]+'0'*(int(b)-len(a[3:])))
        
        
        
                
                
        

    
        
