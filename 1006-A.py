In,Out,person=[],[],[]
n=int(input())
for i in range(n):
    id,ins,out=input().split()
    person.append(id)
    In.append(ins)
    Out.append(out)
unlock=min(In)
index1=In.index(unlock)
lock=max(Out)
index2=Out.index(lock)
print(person[index1],person[index2])
