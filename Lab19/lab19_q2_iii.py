a = [i for i in range(1, 51)]
b = []
for n in range(2, 51):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        b.append(n)
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)