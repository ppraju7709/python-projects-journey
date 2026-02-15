print("-----Volume Calculator-----")

def cube():
    s = int(input("Enter side :"))
    vol = s*s*s
    print("The Volume of cube is ",vol)

def cone():
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    vol = b*h
    print("The Volume of cone is ",vol)

def rectangular_prism():
    l = int(input("Enter length :"))
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    vol = l*b*h
    print("The Volume of Rectangular prism is ",vol)

def sphere():
    r = int(input("Enter side :"))
    vol = 1.33*3.14*r*r*r
    print("The Volume of sphere is ",vol)
    
def triangular_pyramid():
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    vol = b*h*3.33
    print("The Volume of Triangular Pyramid is ",vol)

def square_pyramid():
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    vol = b*h*0.33
    print("The Volume of Square Pyramid is ",vol)

def triangular_prism():
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    vol = b*h
    print("The Volume of Triangular Prism is ",vol)

def cylinder():
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    vol = b*h
    print("The Volume of cylinder is ",vol)

def main():

    print("Select shape of the follows to calculate volume")
    print("Choices : \n 1.Cube\n 2.Cone\n 3.Rectangular Prism\n 4.Sphere\n 5.Triangular Pyramid\n 6.Square Pyramid\n 7.Triangular Prism\n 8.Cylinder")
    global choice
    choice = int(input("Enter your choice (1/2/3/4/5/6/7/8):"))

print("___________________________")
main()
if choice==1:
    cube()
elif choice==2:
    cone()
elif choice==3:
    rectangular_prism()
elif choice==4:
    sphere()
elif choice==5:
    triangular_pyramid()
elif choice==6:
    square_pyramid()
elif choice==7:
    triangular_prism()
elif choice==8:
    cylinder()
else:
    print("Invalid Choice...")

q = str(input("Do you want to again calculate volume? (yes/no) :"))
if q=="yes":
    main()
else:
    print("Exit !!!!")