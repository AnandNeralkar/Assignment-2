def CountDigit(n):
    cnt=0
    while (n!=0):

        n //=10
        cnt=cnt+1
    return cnt    
     
n=(int(input("Enter the number")))
print("\n")
Count=CountDigit(n) 
print("No of digit ",+Count)