def printPattern(n):

    for i in range(n):                   
        j=1               
        while j<=i+1:
            print(j,end=" ")
            j=j+1

                              
        print("\n")

n=(int(input("Enter the number")))
print("\n")
printPattern(n) 