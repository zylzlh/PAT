s=input().split()
n=int(s[0])
sum=0
row=0
while sum<=n:
        row+=1
        sum=2*row**2-1
row-=1
sum=2*row**2-1
left=n-sum
for i in range(row):
        print('{0: ^{1}}'.format(s[1]*(2*(row-i)-1),2*row-1))
for i in range(2,row+1):
        print('{0: ^{1}}'.format(s[1]*(2*i-1),2*row-1))
print(left)
                
        

    
        
