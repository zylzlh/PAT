a,b,d=map(int,input().split())
c=a+b
out=''
if c<d:
        print(c)
else:
        while c>=d:
                r=c%d
                out=str(r)+out
                c//=d
        out=str(c)+out
        print(out)
        

    
        
