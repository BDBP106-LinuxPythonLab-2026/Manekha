L = [1, 2, 3, 2, 4, 2]
x = int(input("Enter element to remove: "))

while x in L:
    L.remove(x)

print(L)