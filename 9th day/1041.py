s=input().lower()
num=[0]*26
for i in range(len(s)):
        if 'a'<=s[i]<='z':
                j=ord(s[i])-ord('a')
                num[j]+=1
a=max(num)
b=chr(num.index(a)+ord('a'))
print(b,a)
        
        
        
        

    
        
