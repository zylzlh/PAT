import re
s=re.sub('\.',' ',input()).split()
a=list(map(int,s))
sum=(a[3]-a[0])*29*17+(a[4]-a[1])*29+a[5]-a[2]
fuhao=0
if sum<0:
        fuhao=1
        sum=abs(sum)
knut=sum%29
sickle=sum//29%17
galleon=sum//(29*17)
if fuhao:
        print('-{}.{}.{}'.format(galleon,sickle,knut))
else:
        print('{}.{}.{}'.format(galleon,sickle,knut))
        

    
        
