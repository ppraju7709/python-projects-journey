# Fibonacci Series Generator

terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print("Fibonacci Series:")
    print(0)
else:
    a, b = 0, 1
    print("Fibonacci Series:")

    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b