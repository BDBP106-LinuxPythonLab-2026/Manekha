names = ["Asha", "Ravi", "Meera", "Arun", "Divya"]

#a:
upper_names = [name.upper() for name in names]
print(upper_names)

#b:
swapped_names = [" ".join(name.split()[::-1]) for name in names]
print(swapped_names)

#c:
formatted_names = [
    ".".join([part.capitalize() for part in name.split()])
    for name in names
]
print(formatted_names)