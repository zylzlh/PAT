s=input()
a=['P','A','T','e','s','t']
b=[0]*6
count=0
for i in range(len(s)):
        for j in range(6):
                if s[i]==a[j]:
                        b[j]+=1
                        count+=1
while count:
        for j in range(6):
                if b[j]!=0:
                        print(a[j],end='')
                        b[j]-=1
                        count-=1
                        
        
        

    
        
