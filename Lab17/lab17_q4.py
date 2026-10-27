N = int(input("Enter a number: "))

if N < 0:
    N = -N

if N == 0:
    print(0)
else:
    while N > 0:
        digit = N % 10
        print(digit)
        N = N // 10