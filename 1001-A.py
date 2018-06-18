a,b=map(int,input().split())
c=str(a+b)
if c[0]=='-':
    k=[4,2,3]
else:
    k=[3,1,2]
l=len(c)
if l<=k[0]:
    print(c)
    exit()
r=l%3
if (k[0]==4 and r==1) or (k[0]==3 and r==0):
    i=k[0]
elif (k[0]==4 and r==2) or (k[0]==3 and r==1):
    i=k[1]
else:
    i=k[2]
print(c[0:i]+',',end='')
while len(c[i:])>3:
    print(c[i:i+3]+',',end='')
    i+=3
print(c[i:])
