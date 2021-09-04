x = int(input("enter the number"))
y = int(input("enter the number"))
z = int(input("enter the number"))
if x>=y and x>=z:
    print("the greatest number is",x)
if y>=x and y>=z:
    print("the greatest number is",y)
if z>=x and z>=y:
    print("the greatest number is",z)