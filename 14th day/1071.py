t,k=map(int,input().split())
while t and k:
    s=list(map(int,input().split()))
    if s[2]>t:
        print('Not enough tokens.  Total = {}.'.format(t))
    elif (s[0]<s[3] and s[1]==1) or (s[0]>s[3] and s[1]==0) :
        t+=s[2]
        print('Win {}!  Total = {}.'.format(s[2],t))
    else:
        t-=s[2]
        print('Lose {}.  Total = {}.'.format(s[2],t))
    k-=1       
if t==0 and k!=0:
    print('Game Over.')
                

        
        
        
        

    
        
