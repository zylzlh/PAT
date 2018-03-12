s=[chr(i) for i in range(ord('a'),ord('z')+1)]
string=input().lower()
sum=0
for i in string:
        if 'a'<=i<='z':
                sum+=s.index(i)+1
k,j=0,0
while sum:
        a=sum%2
        sum//=2
        if a:
                k+=1
        else:
                j+=1
print(j,k)       

                

        
        
        
        

    
        
