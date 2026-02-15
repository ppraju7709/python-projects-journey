a = int(input("Enter 1st no. :"))
b = int(input("Enter 2nd no. :"))
c = int(input("Enter 3rd no. :"))

if a>b & a>c :
    print(a,"is the largest no. among all.")

elif b>a & b>c :
    print(b,"is the largest no. among all.")

elif c>b & c>a :
    print(c,"is the largest no. among all.")

else:
    print("All numbers are equal.")