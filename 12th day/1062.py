def g(i,j):
        d=i%j
        while d!=0:
                i=j
                j=d
                d=i%j
        if j!=1:
                return False
        else:
                return True
a=input().split()
n1,n2=map(eval,a[0:2])
fenmu=int(a[2])
i=1
a=min(n1,n2)
b=max(n1,n2)
c=[]
while b>(i/fenmu):
        if i/fenmu>a and g(i,fenmu):
                c.append(str(i)+'/'+str(fenmu))
        i+=1
print(' '.join(c))
                
                

        
        
        
        

    
        
