print("-----Blood Donation eligibility calculator-----")

nm = str(input("Enter your name :"))
age = int(input("Enter your age :"))
weight = int(input("Enter your weight :"))

if age >= 18:
    if weight >= 45:
        print(nm," are eligible for Blood Donation.")
    else:
        print("The 45+ kg weight is required, try after few months.")
else:
    print("The minimum required age is 18, but you don't fullfiled the criteria.")

