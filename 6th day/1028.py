n=int(input())
youngest='1814/09/06'
oldest='2014/09/06'
count=0
for i in range(n):
        name,birthday=input().split()
        if birthday<'1814/09/06' or birthday>'2014/09/06':
                count+=1
        else:
                if birthday<oldest:
                        oldest=birthday
                        oldestMan=name
                if birthday>youngest:
                        youngest=birthday
                        youngestMan=name
if count<n:
        print('{} {} {}'.format(n-count,oldestMan,youngestMan))
else:
        print('0')
                
        

    
        
