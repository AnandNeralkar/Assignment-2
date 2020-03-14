def Factors(x):
    if(x<=0):
        return 0

    i=1
    total=0
    while(x>i):
            if(x%i==0):                  
                total=total + i               
            i=i+1
    return total


x=(int(input("Enter the  number")))    
factors=Factors(x)
print(factors)