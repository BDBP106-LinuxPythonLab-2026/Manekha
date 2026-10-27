celsius = (0, 25, 37, 100)
fahrenheit = map(lambda c: (9 / 5) * c + 32, celsius)
print(list(fahrenheit))