x = int(input("Enter an hour between 1 to 12 :-"))
y = int(input("Enter Number of hours ahead :-"))
z = x + y
if z <= 12 :
    print("Time is ",z,"o clock")
else :
    print("Time is ",z - 12,"o clock")