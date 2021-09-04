x = int(input("enter the number"))
y = input("a or c")
if y=='a':
    z = 3.14*x**2
    print("the area is",z)
elif y=='c':
        z = 2*3.14*x
        print("the circumference is",z)
else:
        print("wrong entry")