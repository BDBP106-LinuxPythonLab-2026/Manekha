def triangle_type(a, b, c):
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print(triangle_type(5, 5, 5))
print(triangle_type(5, 5, 3))
print(triangle_type(3, 4, 5))