a=input().split()
b=input().split()
poly={}
for i in range(1,len(a),2):
    poly[a[i]]=float(a[i+1])
for i in range(1,len(b),2):
    try:
        poly[b[i]]+=float(b[i+1])
    except:
        poly[b[i]]=float(b[i+1])
c=sorted(poly.items(),key=lambda a: a[0],reverse=True)
d=[]
for i in range(len(c)):
    if c[i][1]!=0:
        d.append(c[i][0])
        d.append(str(c[i][1]))
if len(d)!=0:
    print(int(len(d)/2),' '.join(d))
else:
    print(0)
    
