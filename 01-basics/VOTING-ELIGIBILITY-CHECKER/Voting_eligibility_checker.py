print("-----Voting eligibility calculator-----")

nm = str(input("Enter your name :"))
age = int(input("Enter your age :"))


if age >= 18:
    print(nm," you are eligible for Voting.")

else:
    print("The minimum required age is 18, you don't fullfiled the criteria.")