def rank(person):
        return -int(person[1]),person[0]
n,k=map(int,input().split())
info=[]
for i in range(n):
        info.append(input().split())
order=sorted(info,key=rank)
hang,last=n//k,n//k+n%k
b=[]
sum=0
for i in range(n):
        if sum%2==0:
                b.append(order[i][0])
        else:
                b.insert(0,order[i][0])
        sum+=1
        if sum==last:
                print(' '.join(b))
                last=hang
                b=[]
                sum=0

        
        
        
        

    
        
