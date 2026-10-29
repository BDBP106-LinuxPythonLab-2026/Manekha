import math

def population_growth(initial, rate, time):
    def exponential_growth():
        return initial + math.exp(rate * time)

    population = exponential_growth()
    print("Population after growth:", round(population))

population_growth(1000, 0.05, 10)