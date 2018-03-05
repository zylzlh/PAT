realWord=list(input().upper())
getWord=set(input().upper())
brokenKey=[]
for i in range(len(realWord)):
        if realWord[i] not in getWord and realWord[i] not in brokenKey:
                brokenKey.append(realWord[i])
print(''.join(brokenKey))

                
        

    
        
