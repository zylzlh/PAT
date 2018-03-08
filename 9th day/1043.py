import re
huo=[]
num=[]
gao=['tret','tam','hel','maa','huh','tou','kes','hei','elo','syy','lok','mer','jou']
di=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug',' sep', 'oct',' nov',' dec']
for i in range(169):
        n=i//13
        r=i%13
        if i%13==0:
                huo.append(gao[n])
        elif 0<i<13:
                huo.append(di[r-1])
        else:
                huo.append(gao[n]+' '+di[r-1])
        num.append(str(i))
c=[(x,y) for x,y in zip(num,huo)]        
s=int(input())
for i in range(s):
        a=input()
        if re.match('[\d]',a):
                k=num.index(a)
                print(c[k][1])
        else:
                k=huo.index(a)
                print(c[k][0])
        
                

        
        
                        
        
        

    
        
