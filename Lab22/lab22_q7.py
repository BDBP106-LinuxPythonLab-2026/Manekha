import time
import math

def measure_time(func):
    def wrapper(initial, rate, time_period):
        start = time.time()
        func(initial, rate, time_period)
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper


@measure_time
def population_growth(initial, rate, time_period):
    def exponential_growth():
        population = initial

        for i in range(1000000):
            population = initial + math.exp(rate * time_period)

        return population

    result = exponential_growth()
    print("Population after growth:", round(result))

population_growth(1000, 0.05, 10)