n=int(input())
youngest='1814/09/06'
oldest='2014/09/06'
count=0
for i in range(n):
        s=input().split()
        if s[1]<'1814/09/06' or s[1]>'2014/09/06':
                count+=1
        else:
                if s[1]<oldest:
                        oldest=s[1]
                        oldestMan=s[0]
                if s[1]>youngest:
                        youngest=s[1]
                        youngestMan=s[0]
if count<n:
        print('{} {} {}'.format(n-count,oldestMan,youngestMan))
else:
        print('0')
                
        

    
        
