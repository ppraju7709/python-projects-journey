def condition():
    global num 
    num = int(input("\nEnter the number :"))

    if num % 2 == 0 :
        print("Given Number ", num," is Even")
    elif num % 2 != 0:
        print("Given Number ",num," is Odd")
    else:
        print("Invalid Input, Try Again !")
    que()

def que():        
    Q1 = str(input("\nDo you want to check the given number is Even or Odd ? (Yes/No)"))
    if Q1 == "Yes":
        condition()
    else:
        print("Thank you for visiting us!")
print("\nWelcome in Even or Odd number Checker...")
que()
