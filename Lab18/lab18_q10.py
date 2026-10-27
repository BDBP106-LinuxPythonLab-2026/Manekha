def nextPrime(n):
    candidate = n + 1

    while True:
        isPrime = True

        if candidate < 2:
            isPrime = False
        else:
            for divisor in range(2, candidate):
                if candidate % divisor == 0:
                    isPrime = False
                    break

        if isPrime:
            return candidate

        candidate = candidate + 1

n = int(input("Enter an integer: "))
print(nextPrime(n))