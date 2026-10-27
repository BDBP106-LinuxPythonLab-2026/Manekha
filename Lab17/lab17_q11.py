L = [1, 2, 3, 2, 4, 1, 1]
duplicates = []

for x in L:
    if L.count(x) > 1 and x not in duplicates:
        duplicates.append(x)

print(duplicates)