x = int(input("Enter the number of items purchased"))
if x<10:
    z = x*120
    print("Total cost is",z)
elif x>10 and x<99:
    z = x*100
    print("Total cost is",z)
elif x>=100:
    z = x*70
    print("Total cost is",z)
print("Number of items bought",x)