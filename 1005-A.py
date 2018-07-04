Ch2En=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
n=[int(i) for i in list(input())]
he=[int(i) for i in str(sum(n))]
out=[]
for i in he:
    out.append(Ch2En[i])
print(' '.join(out))

    
