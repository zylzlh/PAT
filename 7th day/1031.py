n=int(input())
d={}
for i in range(n):
        a=input().split()
        try:
                if d[a[0]]:
                        d[a[0]]+=int(a[1])
        except:
                d[a[0]]=int(a[1])
s=sorted(d.items(),key=lambda e:e[1],reverse=True)
print(s[0][0],s[0][1])
                

                
        

    
        
