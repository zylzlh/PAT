def change(a):
        if a=='B':
                return 0
        elif a=='C':
                return 1
        else:
                return 2
result_1=[0,0,0]
result_2=[0,0,0]
hand_1=[0,0,0]
hand_2=[0,0,0]
n=int(input())
for n in range(n):
        a,b=map(change,input().split())
        if (a+1)%3==b:
                result_1[0]+=1
                result_2[2]+=1
                hand_1[a]+=1
        elif a==b:
                result_1[1]+=1
                result_2[1]+=1
        else:
                result_1[2]+=1
                result_2[0]+=1
                hand_2[b]+=1
list1=['B','C','J']
k1,k2=0,0
for i in range(3):
        if hand_1[i]>hand_1[k1]:
                k1=i
        if hand_2[i]>hand_2[k2]:
                k2=i
print('{} {} {}'.format(*result_1))
print('{} {} {}'.format(*result_2))
print('{} {}'.format(list1[k1],list1[k2]))

        
    
                
        

    
        
