n=int(input())
score=list(map(int,input().split()))
s=list(map(int,input().split()))
a=[0]*101
for i in range(len(score)):
        a[score[i]]+=1
for i in range(s[0]-1):
        print(a[s[i+1]],end=' ')
print(a[s[-1]])

        

    
        
