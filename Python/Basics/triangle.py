a = int(input("enter one side of triangle"))
b = int(input("enter second side of triangle"))
c = int(input("enter third side of triangle"))
if a+b>c and b+c>a and c+a>b:
    print("It is a Triangle")
else:
    print("It is not a Triangle")