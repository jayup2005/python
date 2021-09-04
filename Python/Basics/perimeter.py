x = int(input("enter the number"))
y = input("a or p")
if y=='a':
    z = x**2
    print("area is",z)
elif y=='p':
        z = 4*x
        print("perimeter is",z)
else:
        print("wrong entry")