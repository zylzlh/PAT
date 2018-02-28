k=int(input())
x=list(map(int,input().split()))
outer=set()
num=set()
for i in x:
    outer.add(i)
    while i!=1:
        if i in num:
            if i in outer:
                outer.remove(i)
            break
        else:
            num.add(i)
        if i%2:
            i=(i*3+1)/2
        else:
            i/=2
s=[i for i in outer]
s.sort(reverse=True)
for i in range(len(s)-1):
    print(s[i],end=' ')
print(s[-1])
