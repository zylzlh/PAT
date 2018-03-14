n=input().split()  
i=0  
while True:  
    a=input()  
    if a=="#":  
        exit()  
    if a==n[0]:  
        print("Welcome in")  
        exit()  
    else:  
        print("Wrong password: %s" % a) 
        i+=1
    if i==int(n[1]):  
        print("Account locked")  
        exit()
        
            
        
                

        
        
        
        

    
        
