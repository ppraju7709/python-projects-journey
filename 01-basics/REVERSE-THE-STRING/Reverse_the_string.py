# Reverse a String

text = input("Enter a string: ")
reversetext = ""

for char in text:
    reversetext = char + reversetext

print(f"Reversed string: {reversetext}")