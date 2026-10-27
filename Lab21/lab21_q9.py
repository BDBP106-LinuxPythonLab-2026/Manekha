import math

def population_growth(initial, rate, time):
    def exponential_growth():
        population = initial + math.exp(rate * time)
        return population
    result = exponential_growth()
    return result


initial_population = float(input("Enter initial population: "))
growth_rate = float(input("Enter growth rate: "))
elapsed_time = float(input("Enter time: "))

final_population = population_growth(
    initial_population, growth_rate, elapsed_time
)

print("Final population:", round(final_population, 2))