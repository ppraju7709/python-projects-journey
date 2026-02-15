# BODY MASS INDEX CALCULATOR

# BMI = weight (kg) / (height (m) × height (m))
print("-----------BMI Calculator---------------")

weight = int(input("Enter your weight in kg :"))
height = int(input("Enter your height in m :"))
age = int(input("Enter age here :"))

BMI = weight / (height * height)
print("BMI Index =",BMI)

if BMI < 18.5:
    print("You are Underweighted")
elif BMI < 25:
    print("You are Normal")
elif BMI < 30:
    print("You are overweighted")
else:
    print("You are obese")