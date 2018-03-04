n=input()
if len(n)<4:
        n='0'*(4-len(n))+n
if n[0]==n[1]==n[2]==n[3]:
        print('{} - {} = 0000'.format(n,n))
        exit()
def f(x):
        a=''.join(sorted(x))
        b=a[::-1]
        c=str(int(b)-int(a))
        if len(c)<4:
                c='0'*(4-len(c))+c
        print('{} - {} = {}'.format(b,a,c))
        if c=='6174':
                return
        else:
                f(c)
f(n)

        
    
                
        

    
        
