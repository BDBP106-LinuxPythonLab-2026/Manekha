def celsius_to_fahrenheit(c):
    return (9 / 5) * c + 32

celsius = (0, 25, 37, 100)
fahrenheit = map(celsius_to_fahrenheit, celsius)
print(list(fahrenheit))