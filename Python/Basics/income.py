x = int(input("enter the income"))
if x<250000:
    print("no tax")
elif x>250000 and x<500000:
    z = 5*x/100
    print("5% tax is",z)
elif x>500000 and x<1000000:
    z = 20*x/100
    print("10% tax is",z)
elif x>1000000:
    z = 30*x/100
    print("30% tax is",z)