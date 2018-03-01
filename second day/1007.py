from math import sqrt
def is_prime(n):
    if n>=2:
        if n==2:
            return True
        elif n%2==0:
            return False
        for i in range(3,int(sqrt(n))+1,2):
            if n%i==0:
                return False
        return True
    return False
n=int(input())
count=0
for i in range(3,n+1,2):
  if i+2<=n and is_prime(i) and is_prime(i+2):
    count+=1
print(count)

    
                
        

    
        
