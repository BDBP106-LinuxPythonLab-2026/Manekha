python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]

python_students = set(python_class)
java_students = set(java_class)

# Students enrolled in both courses:
both = python_students & java_students
print("Students in both courses:", sorted(both))

# Students enrolled only in Python:
only_python = python_students - java_students
print("Students only in Python:", sorted(only_python))

# Students enrolled in exactly one course:
exactly_one = python_students ^ java_students
print("Students in exactly one course:", sorted(exactly_one))

# All unique students:
all_students = python_students | java_students
print("All students:", sorted(all_students))

# Search for a student:
name = input("Enter a student's name: ").strip()

if name in python_students and name in java_students:
    print(name, "is enrolled in both Python and Java.")
elif name in python_students:
    print(name, "is enrolled in Python only.")
elif name in java_students:
    print(name, "is enrolled in Java only.")
else:
    print(name, "is not enrolled in either course.")