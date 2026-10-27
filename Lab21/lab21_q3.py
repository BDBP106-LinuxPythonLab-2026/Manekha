import math
angles = (0, math.pi / 6, math.pi / 4, math.pi / 2)
result = []

for angle in angles:
    sine = math.sin(angle)
    cosine = math.cos(angle)
    result.append((sine, cosine))

print(result)