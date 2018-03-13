n,m=map(int,input().split())
score=list(map(int,input().split()))
answer=list(map(int,input().split()))
for i in range(n):
        sum=0
        submit=list(map(int,input().split()))
        for j in range(m):
                if submit[j]==answer[j]:
                        sum+=score[j]
        print(sum)
        
                

        
        
        
        

    
        
