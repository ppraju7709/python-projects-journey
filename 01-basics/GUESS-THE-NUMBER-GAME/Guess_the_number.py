import random
print("\nGuess the Number Game")

def conditions():
    n = int(input("\nSelect any random number and enter it :-"))
    if n == x:
        print("\nCongradulations, The Guessed number", n,"is CORRECT" )
    elif x > n:
        print("INCORRECT, Plz Try Again")
        print("\nThe guessed number is greater than the",n) 
        conditions()   
    elif x < n:
        print("INCORRECT, Plz Try Again")
        print("\nThe guessed number is less than the",n) 
        conditions()
    else:
        pass

def que():
    global q1,x
    x = random.randrange(1,100)
    q1 = str(input("Do you want to play the game 'Guess The Number'? (yes/no) : "))
    print("\nGUESS THE ANY NUMBER IN RANGE 1-100") 
    if q1 == "yes" :
        conditions()
        que()
        
    else:
        print("Thank you for enjoying !")

print("Welcome to GUESS THE NUMBER game...")  
que()



