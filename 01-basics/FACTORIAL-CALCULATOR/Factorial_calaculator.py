print("-----Factorial Calculator-----")
n = int(input("Enter the number for Factorial :"))
if n == 0:
    print("0! = 1")    
else:
    for i in range(n,1):
        fact = fact * i
    print("Factorial of ",n," = ",fact)


