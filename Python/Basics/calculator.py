x = int(input("enter the first number"))
y = int(input("enter the second number"))
z = input("A or S or M or Q or R")
if z =='A':
    b = x+y
    print("addition is",b)
elif z =='S':
    b = x-y
    print("subtraction is",b)
elif z =='M':
    b = x*y
    print("multiplication is",b)
elif z =='Q':
    b = x//y
    print("quotient is",b)
elif z =='R':
    b = x%y
    print("remainder is",b)
else:
    print("wrong option")