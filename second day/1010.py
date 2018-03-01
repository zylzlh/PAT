poly=list(map(int,input().split()))
if poly[-1]==0:
    del poly[-2:]
if poly:
    for i in range(0,len(poly),2):
        poly[i]*=poly[i+1]
        poly[i+1]-=1
    for i in range(len(poly)-1):
        print(poly[i],end=' ')
    print(poly[-1])
else:
    print('0','0')

        
    
                
        

    
        
