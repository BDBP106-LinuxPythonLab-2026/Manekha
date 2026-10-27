import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area

a = 3
b = 4
c = 5

print(triangle_area(a, b, c))