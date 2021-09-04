l = int(input("enter length"))
b = int(input("enter breadth"))
y = input("a or p")
if y=='a':
    z = l*b
    print("area is",z)
elif y=='p':
        z = 2*(l+b)
        print("perimeter is",z)
else:
        print("wrong entry")