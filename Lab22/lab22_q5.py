import time

def measure_time(func):
    def wrapper(number):
        start = time.time()
        func(number)
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper


@measure_time
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    print("Factorial of", number, "is:", result)

factorial(50)