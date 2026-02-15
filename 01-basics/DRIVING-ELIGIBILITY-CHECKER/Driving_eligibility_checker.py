print("-----Driving eligibility calculator-----")

nm = str(input("Enter your name :"))
age = int(input("Enter your age :"))


if age >= 18:
    license = str(input("Do you having license? (yes/no) :"))
    if license == "yes":
        print(nm," you are eligible for Driving the vehicle.")
    else:
        print("You don't having a license. So, You are not elgible to drive vehicle.")
else:
    print("The minimum required age is 18, you don't fullfiled the criteria.")
