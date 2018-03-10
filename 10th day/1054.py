n=int(input())
sum,num=0,0
m=input().split()
for i in m:
        try:
                if round(float(i),2)==float(i) and -1000<=float(i)<=1000:
                        num+=1
                        sum+=float(i)
                else:
                        print('ERROR: {} is not a legal number'.format(i))
        except:
                print('ERROR: {} is not a legal number'.format(i))
if num==0:
        print('The average of 0 numbers is Undefined')

elif num==1:
        print('The average of {} number is {:.2f}'.format(num,sum))
else:
        print('The average of {} numbers is {:.2f}'.format(num,sum/num))

    
        
