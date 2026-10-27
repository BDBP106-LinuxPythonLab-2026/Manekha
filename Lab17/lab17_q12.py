m1 = [[5, 8], [7, 9]]
m2 = [[1, 3], [2, 4]]

result = []

for i in range(len(m1)):
    row = []
    for j in range(len(m1[i])):
        value = m1[i][j] - m2[i][j]
        row.append(value)
    result.append(row)

print(result)