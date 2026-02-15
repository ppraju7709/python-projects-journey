pin = int(input("Enter your pin :"))
print("Pin is setted")
code = int(input("Enter pin : "))
while pin != code :
    print("Incorrect pin, Try again.")
    code = int(input("Enter pin : "))
print("LOCK completely unlocked...")