print("_____________ Grade Calculator _____________")

def grade_calculator():
    if 90 <= marks <= 100:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif 0 <= marks < 50:
        grade = "Fail"
    else:
        grade = "Invalid Marks"

    print(subject, "Grade :-", grade)


total_marks = 0
n = int(input("Enter total no. of subjects you have: "))

i = 0
while i != n:
    subject = input("Enter Subject: ")
    marks = int(input("Enter your marks: "))

    grade_calculator()

    if 0 <= marks <= 100:    
        total_marks += marks

    i += 1

percentage = total_marks / n
print("\nTotal Marks:", total_marks)
print("Percentage:", percentage, "%")