#a:
a = [i for i in range(1, 51)]
result = ",".join([str(i) for i in a])
print(result)

#b:
a = [i for i in range(1, 51)]
result = ".".join([str(i) for i in a])
print(result)

#c:
a = [i for i in range(1, 51)]
result = "-".join([str(i) for i in a])
print(result)

#d:
a = [i for i in range(1, 51)]
result = "\n".join([str(i) + " " + str(i**2) for i in a])
print(result)