x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
print("The point is A(",x,",",y,").")
if x>0 and y>0:
    print("It is in first quadrant.")
if x<0 and y>0:
    print("It is in second quadrant.")
if x<0 and y<0:
    print("It is in third quadrant.")
if x>0 and y<0:
    print("It is in fourth quadrant.")