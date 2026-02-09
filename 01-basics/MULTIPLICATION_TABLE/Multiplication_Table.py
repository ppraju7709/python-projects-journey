print("-----Multiplication Table Generator-----")

def table():
    n = int(input("\nEnter which number's table you want ?"))
    i = 1
    for i in range(1,11):
        print(n," X ",i," = ",n*i)
    question()

def question():
    q = str(input("Do you want to build the multiplication table again? (yes/no) :"))
    if q == 'yes':
        table()
    else :
        print("Exiting....!")
    
table()