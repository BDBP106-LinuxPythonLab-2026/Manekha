L = [1, 2, 2, 3, 3, 3, 4, 4]
k = int(input("Enter k: "))

result = []

for x in L:
    if L.count(x) > k and x not in result:
        result.append(x)

print(result)