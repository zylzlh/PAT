import re
n=input()
m=input()
out=''
if '+' in n:
        for i in m:
                if (i<'A' or i>'Z') and i.upper() not in n:
                        out+=i
                        
print(out)       


                
        

    
        
