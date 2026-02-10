# Sum of Digits of a Number

num = int(input("Enter a number: "))

n = abs(num)   # handles negative numbers
sum_of_digits = 0

while n > 0:
    digit = n % 10
    sum_of_digits += digit
    num //= 10

print(f"Sum of digits of {num} is {sum_of_digits}")  #f-string