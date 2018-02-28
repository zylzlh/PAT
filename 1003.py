n=int(input())
students=[]
for i in range(n):
    a=input().split()
    students.append(a)
students.sort(key=lambda s:int(s[2]))
print(students[-1][0],students[-1][1],sep=' ')
print(students[0][0],students[0][1],sep=' ')

      
    
    
