def calculation():
    num1 = float(input("Enter the first no:- "))
    operator = input('Enter operation ( + , - , * , / , % , ** , // ):- ')
    num2 = float(input("Enter the second no:- "))
    
    if operator =='+' :  #Addition
        print("Result =", num1+num2)

    elif operator =='-':    #Substraction
        print("Result =", num1-num2)

    elif operator =='*':   #Multiplication
        print("Result =", num1*num2)

    elif operator =='/':    #Division
        if num2==0:   #if divisor==0
            print("Error, we can divide any number by 0")
            print("plz, Enter another divisor")
            num2 = float(input("Enter the divisor other than 0:- "))
            print("Result =",num1/num2)
        else:    #if divisor!=0
            print("Result =",num1/num2)

    elif operator == '%':   #Modulus
            print("Result =",num1%num2)

    elif operator =='**':   #Exponential
        print("Result =",num1**num2)

    elif operator == '//':  #floor division 
        print("Result =",num1//num2)
    
    else:
        print("Invalid Operator, Try again...")
        calculation()

    Q = input('Do you want to perform more operations? (yes/no) :- ')
    if Q=='yes':
        calculation()
    else:
        print("Thank you for visiting !")

print("Welcome to 'simple Calculator'")
print('Perform the operations as follows')
calculation()