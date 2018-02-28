n=input()
pinyin=['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
sum=0
for i in range(len(n)):
    sum+=int(n[i])
a=str(sum)
for i in range(len(a)-1):
    print(pinyin[int(a[i])],end=' ')
print(pinyin[int(a[-1])])

      
    
    
