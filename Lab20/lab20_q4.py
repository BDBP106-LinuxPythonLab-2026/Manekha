n = int(input("Enter the size of the multiplication table: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(str(i * j).rjust(4), end="")
    print()