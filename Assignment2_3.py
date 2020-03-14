def Factorial(n):

    i=1
         
    if(n<=0):
        return 0

    while n>0:
        i=i*n                  
        n=n-1
    return i

n=(int(input("Enter the number")))
FactorialNo=Factorial(n)
print("Factorial is ",FactorialNo)