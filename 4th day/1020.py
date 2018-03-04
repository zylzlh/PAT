N,D=map(int,input().split())
kuchun=list(map(float,input().split()))
shoujia=list(map(float,input().split()))
rate={i:shoujia[i]/kuchun[i] for i in range(N)}
order=sorted(rate,key=lambda i:rate[i],reverse=True)
money=0
for i in order:
        if D>kuchun[i]:
                money+=shoujia[i]
                D-=kuchun[i]
        else:
                money+=rate[i]*D
                break
print('{0:.2f}'.format(money))
        
    
                
        

    
        
