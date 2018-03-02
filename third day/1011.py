from math import sqrt
m,n=map(int,input().split())
a=3
prime=[2]
count=1
while count<104:
        flag=0
        if a%2==0:
                a+=1
                continue
        else:
                for i in range(3,int(sqrt(a))+1,2):
                        if a%i==0:
                                a+=1
                                flag=1
                                break
        if flag!=1:
                count+=1
                prime.append(a)
                a+=1
k=1
for i in range(m-1,n):
        if k%10!=0 and i<n-1:
                print(prime[i],end=' ')
        else:
                print(prime[i])
        k+=1
        

                
        

    
        
