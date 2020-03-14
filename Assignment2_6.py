def printPattern(n):
          for i in range(n):
                    j=n                
                    while j>i:
                              print("*",end=" ")
                              j-=1
                    print("\n")

x=(int(input("Enter the number")))
print("\n")
printPattern(x) 