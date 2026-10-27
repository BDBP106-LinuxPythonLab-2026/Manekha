def fibonacci(n):
    a = 0
    b = 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series


n = int(input("Enter the number of terms: "))
fib_series = fibonacci(n)
odd_numbers = list(filter(lambda x: x % 2 != 0, fib_series))

print("Fibonacci series:", fib_series)
print("Odd elements:", odd_numbers)