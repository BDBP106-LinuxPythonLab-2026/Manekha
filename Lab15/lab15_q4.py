a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))

root1=(-b+((b*b-4*a*c)**(1/2)))/(2*a)
root2=(-b-((b*b-4*a*c)**(1/2)))/(2*a)

print("The first root is: ",str(root1))
print("The second root is: ",str(root2))

