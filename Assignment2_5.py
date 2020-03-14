def prime(x):
    i=2
    cnt=0
    while(x>=i):
       
        if(x%i==0):
            cnt=cnt+1
           
        i=i+1
    return cnt    
        
x=(int(input("Enter the  number")))
Counter=prime(x)

if(Counter==1):
    print("no is prime")
else:
    print("no is not prime")