from math import sqrt
def prime(x):
        if x>=2:
                if x==2:
                        return True
                if x%2==0:
                        return False
                else:
                        for i in range(3,int(sqrt(x))+1,2):
                                if x%i==0:
                                        return False
                        return True
        else:
                return False
n=int(input())
candidate=[]
for i in range(n):
        candidate.append(input())
k=int(input())
awarded=[]
for i in range(k):
        s=input()
        if s not in candidate:
                print('{}: Are you kidding?'.format(s))
        elif s in awarded:
                print('{}: Checked'.format(s))
        else:
                j=candidate.index(s)+1
                if j==1:
                        print('{}: Mystery Award'.format(s))
                elif prime(j):
                        print('{}: Minion'.format(s))
                else:
                        print('{}: Chocolate'.format(s))
                awarded.append(s)
        
