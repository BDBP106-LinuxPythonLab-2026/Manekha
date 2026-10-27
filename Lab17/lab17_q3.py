N = int(input("Enter a number: "))
isPrime = True

if N < 2:
    isPrime = False
else:
    for divisor in range(2, N):
        if N % divisor == 0:
            isPrime = False
            break

if isPrime:
    print("Prime")
else:
    print("Not prime")