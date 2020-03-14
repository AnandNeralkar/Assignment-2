def SumOfDigit(n):
    cnt=0    
    while (n!=0):
        cnt=cnt+n%10      
        n //=10        
    return cnt    
     
n=(int(input("Enter the number")))
print("\n")
Sum=SumOfDigit(n) 
print("Sum of digit ",+Sum)