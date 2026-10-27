students = [
    ("Asha", 88),
    ("Ravi", 72),
    ("Meera", 95),
    ("Karan", 59),
    ("Divya", 81)
]

total = 0

for name, marks in students:
    total += marks

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(name, ":", marks, "-", grade)

average = total / len(students)
print("Class average:", average)

top_name, top_marks = students[0]
bottom_name, bottom_marks = students[0]

for name, marks in students:
    if marks > top_marks:
        top_name = name
        top_marks = marks

    if marks < bottom_marks:
        bottom_name = name
        bottom_marks = marks

print("Top scorer:", top_name, "-", top_marks)
print("Bottom scorer:", bottom_name, "-", bottom_marks)